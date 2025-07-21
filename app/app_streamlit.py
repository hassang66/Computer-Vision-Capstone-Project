import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import requests

# --- Download model from GitHub if not present ---
@st.cache_resource
def download_and_load_model():
    model_path = "yolov8_gc10_best.pt"
    github_url = "https://raw.githubusercontent.com/hassang66/Computer-Vision-Capstone-Project/main/models/yolov8_gc10_best.pt"

    if not os.path.exists(model_path):
        with st.spinner("Downloading model..."):
            r = requests.get(github_url)
            with open(model_path, 'wb') as f:
                f.write(r.content)

    return YOLO(model_path)

model = download_and_load_model()
