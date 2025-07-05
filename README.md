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

## 🧠 Future Enhancements

- PDF/document reader integration  
- Real-time student progress tracking dashboard  
- Emotion-aware feedback system  
- Multilingual and regional language support  

---

## 👩‍💻 Authors

- Aiswarya Anil  
- Anagha Anil  
- Hima Rose George  
