from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

model_name = "distilbert-base-cased-distilled-squad"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Dummy input for export
inputs = tokenizer("What is AI?", "AI stands for Artificial Intelligence.", return_tensors="pt")

# Export to ONNX
torch.onnx.export(
    model,
    (inputs['input_ids'], inputs['attention_mask']),
    "qa_model.onnx",
    input_names=["input_ids", "attention_mask"],
    output_names=["start_logits", "end_logits"],
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence"},
        "attention_mask": {0: "batch_size", 1: "sequence"}
    },
    opset_version=14
)

print("✅ QA model exported to ONNX successfully.")
