from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
from PIL import Image

# Load model and processor
processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xl", device_map="auto", torch_dtype=torch.float16)

# Load image
image = Image.open("traffic.jpeg").convert("RGB")  # replace with actual filename

# Ask a question
question = "What color is the traffic light?"

# Process inputs
inputs = processor(images=image, text=question, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu", torch.float16)

# Generate answer
output = model.generate(**inputs)
answer = processor.tokenizer.decode(output[0], skip_special_tokens=True)

print("Q:", question)
print("A:", answer)
