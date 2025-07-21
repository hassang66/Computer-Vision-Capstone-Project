import streamlit as st
from PIL import Image
import os
import requests
from ultralytics import YOLO

# --- Constants ---
MODEL_URL = "https://raw.githubusercontent.com/hassang66/Computer-Vision-Capstone-Project/main/models/yolov8_gc10_best.pt"
MODEL_PATH = "yolov8_gc10_best.pt"


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("📥 Downloading model..."):
            response = requests.get(MODEL_URL)
            with open(MODEL_PATH, 'wb') as f:
                f.write(response.content)
    return YOLO(MODEL_PATH)

# --- Streamlit Page Config ---
st.set_page_config(page_title="🛠️ Metal Surface Defect Classifier", layout="centered")
st.title("🛠️ Metal Surface Defect Classifier (GC10 Dataset)")
st.markdown("Upload an image of a metal surface and this app will classify any visible defects using a trained YOLOv8 model.")

# --- Load Model ---
model = load_model()

# --- Upload Interface ---
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="📷 Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Analyzing the image..."):
        results = model.predict(img, conf=0.25)

    # Plot result image
    st.image(results[0].plot(), caption="🔎 Detected Defects", use_container_width=True)

    # --- Display Results ---
    st.subheader("🧠 Prediction Results")
    if len(results[0].boxes) == 0:
        st.info("✅ No defects detected.")
    else:
        for i, box in enumerate(results[0].boxes):
            cls_id = int(box.cls)
            conf = float(box.conf)
            class_name = model.names[cls_id]
            st.markdown(f"**{i+1}. {class_name}** – Confidence: `{conf:.2%}`")

        # Optional summary: most confident prediction
        top_box = max(results[0].boxes, key=lambda b: b.conf)
        top_class = model.names[int(top_box.cls)]
        top_conf = float(top_box.conf)
        st.success(f"🎯 Most confident prediction: **{top_class}** with `{top_conf:.2%}` confidence.")

# --- Footer ---
st.markdown("---")
st.caption("Built using Streamlit and YOLOv8 · Hassan Habib · 2025")
