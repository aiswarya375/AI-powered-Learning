import google.generativeai as genai

genai.configure(api_key="AIzaSyDWS1SzYlYVEOMJ3mrogKmoqJ7Vs_vdLmA")

model = genai.GenerativeModel("models/gemini-1.5-flash")  # or gemini-1.5-pro

def ask_gemini(question, image_context):
    prompt = f"""Here is a description of a diagram:\n{image_context}\n\nQuestion: {question}\nAnswer the questoin """
    response = model.generate_content(prompt)
    return response.text.strip()
