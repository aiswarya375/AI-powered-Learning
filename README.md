# 📚 AI-Powered Learning Assistant

An intelligent, multimodal learning platform that enhances student engagement and understanding through text-based Q&A, image understanding, and speech input. Powered by OpenVINO™-optimized DistilBERT and BLIP models for high-performance inference on edge devices.

---

## 🚀 Features

- **Text Question Answering**  
  Get accurate answers to your queries using a fine-tuned, OpenVINO-optimized DistilBERT model on the SQuAD dataset.

- **Image Captioning**  
  Upload an image and get a natural language description using the OpenVINO-optimized BLIP model.

- **Voice Input Support**  
  Speak your questions using a microphone and let the assistant convert it into text for Q&A.

- **Fast Inference with OpenVINO**  
  All models are accelerated using OpenVINO™ for optimized CPU/GPU performance.

---

## 🛠️ Technologies Used

- **Models**:  
  - `distilbert-base-uncased-distilled-squad` (Text Q&A)  
  - `Salesforce/blip-image-captioning-base` (Image Captioning)

- **Optimization**:  
  - [OpenVINO Toolkit](https://docs.openvino.ai/)

- **Interface**:  
  - Streamlit Web App

- **Languages & Tools**:  
  - Python 3.10+  
  - `transformers`, `optimum`, `speech_recognition`, `torch`, `streamlit`, `Pillow`

---

## 🧩 Folder Structure

ai-learning-assistant/ 

│ 

├── app.py                  
### Streamlit app entry point
├── nlp_module.py           
### Text Q&A logic
├── vision_module.py        
### Image captioning logic
├── speech_module.py         
### Speech-to-text logic 
├── openvino_models/        
### Directory for optimized IR models 
├── requirements.txt        
### Python package dependencies 
└── README.md                
### Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
-bash
git clone https://github.com/your-username/ai-learning-assistant.git
cd ai-learning-assistant

2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate       #Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Export and Optimize Models using OpenVINO

## DistilBERT for Q&A
optimum-cli export openvino \
  --model distilbert-base-uncased-distilled-squad \
  --task question-answering \
  --output openvino_models/distilbert

### BLIP for image captioning
optimum-cli export openvino \
  --model Salesforce/blip-image-captioning-base \
  --task image-to-text \
  --output openvino_models/blip

4. Run the Application

streamlit run app.py


---

## 🧠 Future Enhancements

PDF/document reader integration

Real-time student progress monitoring

Emotion-aware learning

Multilingual and regional language support



---

## 👩‍💻 Authors

Aiswarya Anil
Anagha Anil
Hima Rose George


---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

