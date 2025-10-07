import streamlit as st
import pytesseract
from PIL import Image
import requests
import cv2
import numpy as np

# OpenAI API Key
api_key = "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"

def preprocess_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def extract_text_from_image(image):
    return pytesseract.image_to_string(image, config='--psm 6 --oem 3').strip()

def evaluate_handwriting_sentence(correct_text, headers):
    prompt = f"""As a strict calligraphy expert, evaluate the handwritten sentence '{correct_text}' based on these criteria:
1. **Letter Formation (2 points)**: Are individual letters well-formed and recognizable?
2. **Consistent Letter Size (2 points)**: Are all letters of consistent size across the sentence?
3. **Spacing (2 points)**: Is there appropriate spacing between letters and words?
4. **Overall Aesthetics (2 points)**: Does the sentence have a pleasing, balanced appearance?
Provide a detailed analysis and score out of 8, highlighting strengths and weaknesses. It is very hard to get more than a 6/8 unless near perfection."""

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a strict calligraphy expert."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1024,
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def generate_suggestions(evaluation, correct_text, headers):
    improvement_prompt = f"""Based on this evaluation:\n\n{evaluation}\n\nProvide actionable suggestions to improve the calligraphy of the sentence '{correct_text}'. Keep each suggestion between 7-9 words."""
    
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a calligraphy expert."},
            {"role": "user", "content": improvement_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1024,
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

# Streamlit UI
st.title("Calligraphy Sentence Evaluation Tool")

uploaded_file = st.file_uploader("Upload an image of your handwritten sentence (JPEG/PNG):", type=["jpg", "png", "jpeg"])

if uploaded_file:
    try:
        sentence_image = Image.open(uploaded_file)
        st.image(sentence_image, caption="Uploaded Handwritten Sentence", use_column_width=True)

        st.write("Processing image...")
        binary_image = preprocess_image(sentence_image)
        
        extracted_text = extract_text_from_image(binary_image)
        st.write(f"OCR Extracted Text: {extracted_text}")

        # Allow user to input the correct sentence (limited to 5 words)
        correct_text = st.text_input("Enter the correct sentence :", value=extracted_text)

        # Limit the sentence to 5 words
        correct_text = " ".join(correct_text.split()[:10])

        if st.button("Evaluate Handwriting"):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            evaluation = evaluate_handwriting_sentence(correct_text, headers)
            st.subheader(f"Evaluation for '{correct_text}':")
            st.write(evaluation)

            suggestions = generate_suggestions(evaluation, correct_text, headers)
            st.subheader("Suggestions for Improvement:")
            st.write(suggestions)

    except Exception as e:
        st.error(f"An error occurred: {e}")





        