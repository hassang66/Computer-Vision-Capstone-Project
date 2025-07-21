import streamlit as st
from PIL import Image
from ultralytics import YOLO

model = YOLO("/content/drive/MyDrive/Datasets/yolo_runs/yolov8_gc10_best.pt")

st.title("Metal Defect Detector")
uploaded = st.file_uploader("Upload an image", type=["jpg","png"])
if uploaded:
    img = Image.open(uploaded)
    results = model.predict(source=img)  # or model(img)
    # Display image with bounding boxes
    st.image(results[0].plot(), caption="Detected defects")
    # List classes detected
    for obj in results[0]:
        st.write(f"{obj.name}: {obj.confidence:.2f}")

