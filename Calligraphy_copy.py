import streamlit as st 
import base64
import requests
import os

# Get OpenAI API Key from environment variable
#api_key = os.getenv("OPENAI_API_KEY")
api_key = "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"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# Define the paths for each letter
image_paths = {
    "a": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/a-normal.jpg",
    "b": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/b-1.jpg",
    "c": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/c-1.jpg",
    "d": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/d-1.jpg",
    "e": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/e-1.jpg",
    "f": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/f-1.jpg",
    "g": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/g-1.jpg",
    "h": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/h-1.jpg",
    "i": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/i-1.jpg",
    "j": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/j-1.jpg",
    "k": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/k-1.jpg",
    "l": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/l-1.jpg",
    "m": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/m-1.jpg",
    "n": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/n-1.jpg",
    "o": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/o-1.jpg",
    "p": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/p-1.jpg",
    "q": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/q-1.jpg",
    "r": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/r-1.jpg",
    "s": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/s-1.jpg",
    "t": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/t-1.jpg",
    "u": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/u-1.jpg",
    "v": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/v-1.jpg",
    "w": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/w-1.jpg",
    "x": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/x-1.jpg",
    "y": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/y-1.jpg",
    "z": "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/z-1.jpg"
}

image_path_3 = "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/b-normal.jpg"
letter = st.text_input("Enter the letter you want to analyze:").lower()

if letter != "":
    selected_image = image_paths.get(letter)

    if selected_image:
        # Get the base64 strings for each image
        base64_image_1 = encode_image(selected_image)
        base64_image_3 = encode_image(image_path_3)

        # Now you can use these encoded images for further processing

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"  
    }

    payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are a master calligraphy instructor with decades of experience, known for maintaining exceptionally high standards. You believe in pushing students to achieve perfection through rigorous evaluation. You rarely give perfect scores and actively look for areas of improvement. Even minor flaws should be pointed out and reflected in the scoring."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"""\nThe first image shows the exemplar for the letter {letter} in calligraphy - this represents absolute perfection and should be your reference point. The second image shows a student attempt at writing the letter {letter}. Your task is to critically evaluate the student's work against this exemplar using the criteria below. Remember that perfect scores (2 points) should be extremely rare and reserved only for work that is virtually indistinguishable from the exemplar. Even accomplished calligraphers rarely achieve perfect scores. A total score above 6 should be exceptional and uncommon.

Score the following 4 factors for a maximum total of 8 points. Do not provide any summary or title.

Consistent Stroke Pressure (2 points):
2 points: EXCEPTIONAL (Rare) - Demonstrates masterful pressure control identical to the exemplar. Perfect thick-to-thin ratio of 5:1. Downstrokes must be exactly parallel and upstrokes hairline thin. No pressure variations within individual strokes.
1.5 points: ADVANCED - Shows strong control but falls short of exemplar quality. Thick-to-thin ratio of at least 4:1. Maximum of two minor pressure inconsistencies. All pressure transitions must be smooth.
1 point: INTERMEDIATE - Achieves basic thick-thin contrast (3:1 ratio) but shows multiple pressure control issues. Three to four noticeable pressure inconsistencies.
0.5 points: BEGINNER - Minimal thick-thin contrast (2:1 ratio or less). Five or more pressure inconsistencies. Frequent wobbling in strokes.
0 points: FUNDAMENTAL - No intentional pressure variation. Strokes show random thickness or uniform width throughout.

Cohesive Strokes (2 points):
2 points: EXCEPTIONAL (Rare) - Every stroke matches exemplar's precision. No tremors, wobbles, or hesitations. Perfectly smooth ink flow. Strokes must maintain exact intended width throughout.
1.5 points: ADVANCED - Up to two instances of minor shakiness or width variation. Stroke edges mostly clean but show slight imperfections under magnification.
1 point: INTERMEDIATE - Three to four instances of visible shakiness. Some strokes show obvious width variations or tremors.
0.5 points: BEGINNER - Five or more instances of obvious shakiness. Multiple strokes show significant tremors or hesitation marks.
0 points: FUNDAMENTAL - Majority of strokes show constant tremors or hesitation. No evidence of controlled execution.

Smooth Transitions Between Strokes (2 points):
2 points: EXCEPTIONAL (Rare) - All transitions are flawless. Perfect entry/exit points. No visible stops, starts, or angular connections. Flawless curve continuity.
1.5 points: ADVANCED - Maximum of two slightly imperfect transitions. Entry/exit angles within 5 degrees of ideal. Minor connection issues visible under magnification.
1 point: INTERMEDIATE - Three to four obvious transition issues. Entry/exit angles deviate by 5-15 degrees. Visible stops and starts at connection points.
0.5 points: BEGINNER - Five or more problematic transitions. Entry/exit angles off by more than 15 degrees. Obvious breaks in flow.
0 points: FUNDAMENTAL - Most or all transitions show abrupt changes in direction. No evidence of planned connection points.

Stroke Consistency (2 points):
2 points: EXCEPTIONAL (Rare) - All measurements match exemplar within 0.5mm. Perfect x-height ratio. Slant angle consistent within 1 degree. Spacing exactly matches exemplar.
1.5 points: ADVANCED - Measurements within 1mm of exemplar. X-height ratio within 5% deviation. Slant consistent within 2-3 degrees. Spacing varies by less than 1mm.
1 point: INTERMEDIATE - Measurements deviate 1-2mm from exemplar. X-height ratio varies by 5-10%. Slant varies by 3-5 degrees. Spacing varies by 1-2mm.
0.5 points: BEGINNER - Measurements off by 2-3mm. X-height ratio varies by 10-20%. Slant varies by 5-10 degrees. Spacing varies by 2-3mm.
0 points: FUNDAMENTAL - Measurements deviate more than 3mm. X-height ratio varies by over 20%. Slant varies by over 10 degrees. Spacing varies by over 3mm.

For each category, to award points, you must explicitly confirm that the work matches the exemplar in all measured aspects for that category."""
                },
                # {
                #     "type": "image_url",
                #     "image_url": {
                #         "url": f"data:image/jpeg;base64,{base64_image_1}"
                #     }
                # },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_3}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 2048,
    "temperature": 0.3  # Reduced temperature for more consistent, stricter scoring
}

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    response_json = response.json()

    # Assuming the relevant content is in 'choices' -> 'message' -> 'content'
    calligraphy_output = response_json['choices'][0]['message']['content']

    # Print the calligraphy evaluation content
    st.header("Scoring: ")
    st.write(calligraphy_output)

    second_prompt = f"""Based on the following calligraphy evaluation:\n\n{calligraphy_output}\n\nPlease provide detailed but brief suggestions on how to improve the calligraphy of the letter. : {letter}.Here are the factors you can suggest(do not provide summary at the end):
    1. Consistent Stroke Pressure
    2. Cohesive Strokes
    3. Smooth Transitions Between Strokes
    4. Stroke Consistency
    5. Correct Posture and Rhythm"""

    payload = {
        "model": "gpt-4o-mini", 
        "messages": [
            {"role": "system", "content": "You are a calligraphy expert."},
            {"role": "user", "content": second_prompt}
        ],
        "temperature": 0.7, 
        "max_tokens": 2048 
    }

    second_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    second_response_json = second_response.json()

    suggestions = second_response_json['choices'][0]['message']['content']

    st.header("Suggestions: ")
    st.write(suggestions)