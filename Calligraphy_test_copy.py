import streamlit as st
import base64
import requests
from PIL import Image
import io

# OpenAI API Key
api_key = "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"
# Function to encode an image to Base64
def encode_image(image):
    if image.mode == "RGBA":
        image = image.convert("RGB")
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Function to evaluate the entire word
def evaluate_word(word_image, headers):
    # Encode the word image as Base64
    base64_image = encode_image(word_image)

    # Payload for evaluation
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a master calligraphy expert. Critically evaluate the overall quality of this handwritten word based on strict calligraphy criteria."
            },
            {
                "role": "user",
                "content": """Evaluate the following handwritten word based on the following criteria:
1. Consistent Stroke Pressure (2 points)
2. Cohesive Strokes (2 points)
3. Smooth Transitions Between Strokes (2 points)
4. Stroke Consistency (2 points)
Provide a total score out of 8, highlighting strengths and weaknesses."""
            },
            {
                "role": "user",
                "image": f"data:image/jpeg;base64,{base64_image}"
            }
        ],
        "temperature": 0.3,
        "max_tokens": 2048,
    }

    # Call the API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("Calligraphy Word Evaluation Tool")

# Upload an image of the handwritten word
uploaded_file = st.file_uploader("Upload an image of your handwritten word (JPEG/PNG):", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    word_image = Image.open(uploaded_file)
    st.image(word_image, caption="Uploaded Word Image", use_column_width=True)

    # Evaluate the uploaded image
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    st.write("Evaluating the word...")
    evaluation = evaluate_word(word_image, headers)

    # Display evaluation results
    st.header("Evaluation Results:")
    st.write(evaluation)

    # Generate improvement suggestions
    improvement_prompt = f"""Based on this evaluation:\n\n{evaluation}\n\nProvide actionable suggestions to improve the overall calligraphy of the word."""
    suggestions_payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a calligraphy expert."},
            {"role": "user", "content": improvement_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2048,
    }

    suggestions_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=suggestions_payload)
    if suggestions_response.status_code == 200:
        suggestions = suggestions_response.json()["choices"][0]["message"]["content"]
        st.header("Suggestions for Improvement:")
        st.write(suggestions)
    else:
        st.error(f"Error generating suggestions: {suggestions_response.status_code}")