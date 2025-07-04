from deepface import DeepFace
from PIL import Image
import numpy as np
import cv2

# Emotions considered attentive
ATTENTIVE_EMOTIONS = ["happy", "surprise", "neutral"]

def analyze_image_engagement(uploaded_image):
    img = np.array(uploaded_image.convert("RGB"))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    try:
        results = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
    except Exception as e:
        return "Error analyzing image", []

    # Support for multiple faces
    if isinstance(results, list):
        analysis = []
        for face in results:
            emotion = face["dominant_emotion"]
            status = "Attentive" if emotion in ATTENTIVE_EMOTIONS else "Distracted"
            analysis.append((emotion, status))
        return f"Detected {len(analysis)} student(s)", analysis
    else:
        emotion = results["dominant_emotion"]
        status = "Attentive" if emotion in ATTENTIVE_EMOTIONS else "Distracted"
        return "1 face detected", [(emotion, status)]
