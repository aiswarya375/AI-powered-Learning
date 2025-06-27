from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image

# Load model and processor
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

# Dummy image input
image = Image.new("RGB", (384, 384), color="white")
inputs = processor(images=image, return_tensors="pt")

# Use tokenizer to get BOS (beginning of sentence) token for decoder start
bos_token_id = processor.tokenizer.cls_token_id
decoder_input_ids = torch.tensor([[bos_token_id]])

# Export the model to ONNX
torch.onnx.export(
    model,
    args=(inputs["pixel_values"], decoder_input_ids),
    f="blip_model.onnx",
    input_names=["pixel_values", "decoder_input_ids"],
    output_names=["logits"],
    dynamic_axes={
        "pixel_values": {0: "batch_size"},
        "decoder_input_ids": {0: "batch_size", 1: "seq_len"}
    },
    opset_version=14
)

print("✅ BLIP model exported to ONNX successfully.")
