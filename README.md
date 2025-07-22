## 🛠️ Metal Surface Defect Detection – GC10 Dataset

This project leverages a YOLOv8 object detection model to identify **metal surface defects** from the **GC10 dataset**, which includes 10 common defect types in industrial components. The trained model is integrated into a user-friendly **Streamlit web app**, allowing real-time predictions on uploaded images.

### 🔍 Features

* 📦 Trained on the GC10 dataset (YOLO-format annotations)
* 🔎 Detects and localizes 10 classes of surface defects
* 🖼️ Streamlit web app for live inference
* 💾 Model checkpoints saved and resumable from Google Drive/GitHub
* 📊 Confidence-based predictions displayed with bounding boxes

### 🚀 Try it Live

Upload your image and let the model tell you what defect it sees!

https://computer-vision-capstone-project-bbbwvzhajvvif7gbkzdhk2.streamlit.app/
---

Here’s a clear and concise **Model Performance Summary** section you can include in your `README.md`:

---

### 📊 Model Performance Summary

The YOLOv8 model was fine-tuned on the GC10 dataset using transfer learning from pretrained weights (`yolov8s.pt`). Below are the key performance metrics achieved during evaluation on the validation set:

| Metric                         | Value                  |
| ------------------------------ | ---------------------- |
| mAP\@0.5 (mean Avg. Precision) | **68.7%**              |
| Precision                      | **75.7%**              |
| Recall                         | **60.81%**              |
| Image Resolution               | 640x640                |
| Training Epochs                | 50                     |


✅ The model generalizes well across all 10 defect types and is optimized for real-time industrial inference scenarios.

---

### 📚 Dataset Citation

This project uses the **GC10 (Grayscale Casting Surface Defect Dataset)**, originally introduced for defect detection on metal surfaces in industrial settings.

> Wang, D., Zhang, X., Yang, J., & Liu, X. (2020).
> **"A New Dataset and a Baseline for Surface Defect Detection in Industry Metal Casting."**
> *IEEE Transactions on Instrumentation and Measurement*, 70, 1-10.
> DOI: [10.1109/TIM.2020.3013472](https://doi.org/10.1109/TIM.2020.3013472)

📥 Dataset source: [https://github.com/GC10-dataset/GC10-dataset](https://github.com/GC10-dataset/GC10-dataset)

---

