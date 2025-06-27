# vision_module.py
from transformers import BlipProcessor, BlipForConditionalGeneration, Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch

# Image Captioning (BLIP)
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def describe_image(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = caption_processor(images=image, return_tensors="pt")
    out = caption_model.generate(**inputs)
    return caption_processor.decode(out[0], skip_special_tokens=True)

# Image QnA (BLIP-2)
vqa_processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
vqa_model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl", device_map="auto", torch_dtype=torch.float16)

def answer_vqa(image, question):
    inputs = vqa_processor(images=image, text=question, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu", torch.float16)
    out = vqa_model.generate(**inputs)
    return vqa_processor.tokenizer.decode(out[0], skip_special_tokens=True)
