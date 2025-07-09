# 📚 AI-Powered Learning Assistant  
[🔗 Try the App](https://elearn-aipower.streamlit.app/)

An intelligent, multimodal learning platform that enhances student engagement and understanding through text-based Q&A, image understanding, speech input, and engagement detection. Powered by OpenVINO™-optimized DistilBERT and BLIP models for high-performance inference on edge devices.

---

## 🚀 Features

- **Text Question Answering**  
  Get accurate answers to your queries using a fine-tuned, OpenVINO-optimized DistilBERT model on the SQuAD dataset.

- **Image Captioning**  
  Upload an image and get a natural language description using the OpenVINO-optimized BLIP model.

- **Image Question Answering**  
  Ask questions based on an image and get intelligent answers using BLIP-2 with OpenVINO acceleration.

- **Voice Input Support**  
  Speak your questions using a microphone and let the assistant convert it into text for Q&A.

- **Engagement Detection**  
  Upload classroom images to analyze student attentiveness using head pose estimation, facial orientation, and gaze direction.

- **Fast Inference with OpenVINO**  
  All models are accelerated using OpenVINO™ for optimized CPU/GPU performance.

---

## 🛠️ Technologies Used

- **Models**:  
  - `distilbert-base-uncased-distilled-squad` (Text Q&A)  
  - `Salesforce/blip-image-captioning-base` (Image Captioning)  
  - `Salesforce/blip2-flan-t5-xl` (Image Question Answering)  
  - Custom OpenCV/Dlib-based engagement detection model

- **Optimization**:  
  - [OpenVINO Toolkit](https://docs.openvino.ai/)

- **Interface**:  
  - Streamlit Web App

- **Languages & Tools**:  
  - Python 3.10+  
  - `transformers`, `optimum`, `speech_recognition`, `torch`, `streamlit`, `opencv-python`, `Pillow`, `dlib`

---

## 🧩 Folder Structure

```
ai-learning-assistant/
│
├── app.py                  # Streamlit app entry point
├── nlp_module.py           # Text Q&A logic
├── vision_module.py        # Image captioning and VQA logic
├── speech_module.py        # Speech-to-text logic 
├── engagement_module.py    # Engagement analysis from uploaded classroom images
├── openvino_models/        # Directory for optimized IR models 
├── requirements.txt        # Python package dependencies 
└── README.md               # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-learning-assistant.git
cd ai-learning-assistant
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Export and Optimize Models using OpenVINO

**DistilBERT for Q&A**
```bash
optimum-cli export openvino \
  --model distilbert-base-uncased-distilled-squad \
  --task question-answering \
  --output openvino_models/distilbert
```

**BLIP for Image Captioning**
```bash
optimum-cli export openvino \
  --model Salesforce/blip-image-captioning-base \
  --task image-to-text \
  --output openvino_models/blip
```

**BLIP-2 for Image Question Answering**
```bash
optimum-cli export openvino \
  --model Salesforce/blip2-flan-t5-xl \
  --task visual-question-answering \
  --output openvino_models/blip2
```

### 4. Run the Application
```bash
streamlit run app.py
```

---

## ✅ Outcomes

📚 Personalized Learning: Learners can interact with an AI tutor through voice, text, and image-based queries, enabling personalized educational support.

⚡ Fast Inference with OpenVINO: Optimized DistilBERT and BLIP models reduce latency and improve performance, making real-time feedback possible even on lower-end hardware.

🧠 Knowledge Reinforcement: The new Quiz Module encourages active recall and self-assessment with instant feedback.

🖼️ Multi-modal Interaction: BLIP enables image understanding for visual question answering, enhancing accessibility and creativity in education.

🎙️ Voice Support: Learners who are visually impaired or prefer audio-based learning benefit from speech-based interaction.



---

## 🌟 Future Scope

🔁 Model Fine-Tuning for Subjects: Fine-tune BLIP and DistilBERT on domain-specific educational data (e.g., math, biology, programming).

📊 Student Analytics Dashboard: Track student progress, quiz performance, time spent, and learning patterns.

🌐 Multilingual Support: Integrate translation + multilingual models for students in regional or non-English-speaking areas.

👩‍🏫 Teacher/Admin Panel: Allow educators to add content, monitor usage, and upload image-based assignments.

🤝 Collaborative Learning Mode: Enable peer-to-peer question exchange and group quiz sessions.

📱 Mobile App Version: Launch a lightweight Android/iOS version using TFLite + OpenVINO backend.



---

## ⚠️ Limitations

🧠 Model Generalization: BLIP and DistilBERT might misinterpret questions outside their pretraining domain (e.g., niche academic topics).

🌐 Internet Dependency: Some parts (e.g., fetching online content, model downloading) may need internet unless pre-cached.

🖥️ System Requirements: While OpenVINO reduces inference cost, initial setup and local running still require a reasonably capable machine.

🗣️ Speech Accuracy: Quiz and voice modules may have lower accuracy in noisy environments or with strong accents.

💾 Storage for Models: ONNX/OpenVINO models (100MB+) may pose storage issues without proper file hosting or model compression.

---


## 👩‍💻 Authors

- Aiswarya Anil  
- Anagha Anil  
- Hima Rose George  
