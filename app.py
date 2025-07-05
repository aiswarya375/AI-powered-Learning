
import streamlit as st
from PIL import Image
import os
import random

from nlp_module import answer_question
from speech_module import speech_to_text
from vision_module import answer_vqa # describe_image
from llama_index.llms.openvino import OpenVINOLLM
from llama_index.core import ServiceContext
from llama_index.core.llms import ChatMessage
from langchain_mistralai import ChatMistralAI
from langchain.prompts import PromptTemplate

# Initialize openvino LLM
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
    api_key="MISTRAL_API_KEY" #Here add your created api key
)

quiz_prompt = PromptTemplate.from_template(
    """
    You are a quiz generator. Create a quiz with 10 multiple-choice questions on the topic: {topic}.
    For each question, provide 4 options and indicate the correct option clearly.
    The format should be:

    Q1. Question text
    a) option1
    b) option2
    c) option3
    d) option4
    Answer: b

    Continue this format for all 10 questions.
    """
)



st.set_page_config(page_title="AI Learning Assistant", layout="centered")
st.title("🎓 AI-Powered Learning Assistant")

st.sidebar.title("Modes")
mode = st.sidebar.radio("Choose Input Type", [
    "Text", 
    "Voice", 
    "Image Captioning", 
    "Image Question Answering", 
    "Engagement Detection",
    "Take Quiz"
])




if mode == "Text":
    question = st.text_input("Ask your question:")
    context = st.text_area("Provide context (like a paragraph from textbook):")
    if st.button("Get Answer") and question and context:
        answer = answer_question(question, context)
        st.success(f"📘 Answer: {answer}")

elif mode == "Image Captioning":
    uploaded_img = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_img:
        image = Image.open(uploaded_img)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img_path = f"temp_{uploaded_img.name}"
        image.save(img_path)
        caption = describe_image(img_path)
        os.remove(img_path)

        st.success(f"🖼️ Caption/Interpretation: {caption}")

elif mode == "Image Question Answering":
    uploaded_img = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    question = st.text_input("Ask a question about the image:")

    if uploaded_img and question:
        image = Image.open(uploaded_img).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        answer = answer_vqa(image, question)
        st.success(f"🧠 Answer: {answer}")

elif mode == "Engagement Detection":
    st.warning("Engagement detection module is not yet implemented.")


elif mode == "Voice":
    context = st.text_area("Provide context (like a paragraph from textbook):")
    if st.button("🎤 Record and Answer") and context:
        transcribed = speech_to_text()
        if transcribed:
            st.write("🗣️ You asked:", transcribed)
            answer = answer_question(transcribed, context)
            st.success(f"📘 Answer: {answer}")

elif mode == "Take Quiz":
    st.title("Quiz Generator")
    st.write("Enter a topic, generate a quiz, and test yourself!")

    # Session state to store quiz
    if 'quiz' not in st.session_state:
        st.session_state.quiz = []
        st.session_state.answers = []
        st.session_state.correct_answers = []
        st.session_state.evaluated = False
        st.session_state.show_answers = False

    # Input Topic
    topic = st.text_input("Enter a quiz topic:")

    if st.button("Generate Quiz"):
        if not topic.strip():
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating quiz..."):
                st.session_state.evaluated = False
                st.session_state.show_answers = False
                prompt = quiz_prompt.format(topic=topic)
                response = llm.invoke(prompt).content

                # Parse Questions
                questions = response.strip().split("\n\n")
                parsed_quiz = []
                correct_answers = []

                for q in questions:
                    lines = q.strip().split("\n")
                    if len(lines) < 6:
                        continue  # Skip incomplete question
                    question_text = lines[0]
                    options = lines[1:5]
                    answer_line = lines[5]
                    correct_option = answer_line.split(":")[-1].strip().lower()

                    parsed_quiz.append({
                        "question": question_text,
                        "options": options,
                    })
                    correct_answers.append(correct_option)

                if len(parsed_quiz) == 10:
                    st.session_state.quiz = parsed_quiz
                    st.session_state.correct_answers = correct_answers
                    st.session_state.answers = [''] * 10
                else:
                    st.error("Failed to generate 10 valid questions. Please try again.")

    # Display Quiz
    if st.session_state.quiz:
        st.subheader("Your Quiz")

        for idx, q in enumerate(st.session_state.quiz):
            st.write(f"**{q['question']}**")
            options_text = [opt.split(') ')[1] for opt in q['options']]  # Extract only option text

            selected = st.radio(
                f"Select your answer for Question {idx + 1}:",
                options_text,
                index=options_text.index(st.session_state.answers[idx]) if st.session_state.answers[idx] in options_text else 0,
                key=f"question_{idx}",
                disabled=st.session_state.evaluated
            )
            st.session_state.answers[idx] = selected

        if not st.session_state.evaluated and st.button("Submit Quiz"):
            score = 0
            for user_ans, correct_ans_key, q in zip(st.session_state.answers, st.session_state.correct_answers, st.session_state.quiz):
                options_text = [opt.split(') ')[1] for opt in q['options']]
                correct_option_text = options_text[['a', 'b', 'c', 'd'].index(correct_ans_key.lower())]

                if user_ans.strip().lower() == correct_option_text.strip().lower():
                    score += 1

            st.success(f"You got {score} out of 10 correct!")
            st.session_state.evaluated = True

        # Show Correct Answer Button
        if st.session_state.evaluated and not st.session_state.show_answers:
            if st.button("Show Correct Answers"):
                st.session_state.show_answers = True

        # Show correct answers
        if st.session_state.show_answers:
            st.subheader("Correct Answers")
            for idx, q in enumerate(st.session_state.quiz):
                options_text = [opt.split(') ')[1] for opt in q['options']]
                correct_option_text = options_text[['a', 'b', 'c', 'd'].index(st.session_state.correct_answers[idx].lower())]
                st.info(f"Q{idx + 1}: **{correct_option_text}**")

