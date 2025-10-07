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
    "a": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/a-normal.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/a-calligraphy.jpg",
    ],
    "b": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/b-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/b-2.jpg",
    ],
    "c": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/c-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/c-2.jpg",
    ],
    "d": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/d-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/d-2.jpg",
    ]
    ,
    "e": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/e-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/e-2.jpg",
    ],
    "f": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/f-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/f-2.jpg",
    ],
    "g": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/g-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/g-2.jpg",
    ],
    "h": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/h-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/h-2.jpg",
    ],
    "i": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/i-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/i-2.jpg",
    ],
    "j": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/j-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/j-2.jpg",
    ],
    "k": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/k-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/k-2.jpg",
    ],
    "l": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/l-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/l-2.jpg",
    ],
    "m": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/m-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/m-2.jpg",
    ],
    "n": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/n-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/n-2.jpg",
    ],
    "o": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/o-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/o-2.jpg",
    ],
    "p": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/p-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/p-2.jpg",
    ],
    "q": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/q-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/q-2.jpg",
    ],
    "r": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/r-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/r-2.jpg",
    ],
    "s": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/s-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/s-2.jpg",
    ],
    "t": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/t-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/t-2.jpg",
    ],
    "u": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/u-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/u-2.jpg",
    ],
    "v": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/v-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/v-2.jpg",
    ],
    "w": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/w-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/w-2.jpg",
    ],
    "x": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/x-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/x-2.jpg",
    ],
    "y": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/y-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/y-2.jpg",
    ],
    "z": [
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/z-1.jpg",
        "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/z-2.jpg",
    ]
}

image_path_3 = "/Users/pranatialladi/Desktop/Calligraphy_Folder/images/e-normal.jpg"

letter = input("Please enter the letter you want to analyze: ").lower()
selected_images = image_paths.get(letter)

if selected_images:
    # Get the base64 strings for each image
    base64_image_1 = encode_image(selected_images[0])
    base64_image_2 = encode_image(selected_images[1])
    base64_image_3 = encode_image(image_path_3)

    # Now you can use these encoded images for further processing
else:
    letter = input("Please enter the letter you want to analyze: ")

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
          "text": "You are an expert at teaching calligraphy."
        }
      ]
    },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"""\nThe first two images are the proper way to write the letter\n\n{letter}\n\n in calligraphy. The third image is \n my attempt at writing the letter \n\n{letter}\n\n in calligraphy. Compare my calligraphy letter \n\n{letter}\n\n" with the proper way using the following judging factors. Based on the following 4 factors, give me a total score out of 8.\n\nConsistent Stroke Pressure (2 points)\n2 points: Perfect contrast between thick downstrokes and thin upstrokes\n1.5 points: Good contrast, but occasional inconsistencies\n1 point: Some contrast, but frequent inconsistencies\n0.5 points: Little contrast between upstrokes and downstrokes\n0 points: No discernible difference in stroke pressure\nCohesive Strokes (2 points)\n2 points: Perfectly uniform and smooth strokes throughout\n1.5 points: Mostly uniform strokes with minor irregularities\n1 point: Some uniformity, but noticeable inconsistencies\n0.5 points: Frequent irregularities in stroke width and flow\n0 points: Highly irregular strokes with no cohesion\nSmooth Transitions Between Strokes (2 points)\n2 points: Flawless, fluid connections between all letters\n1.5 points: Mostly smooth transitions with occasional minor hitches\n1 point: Some smooth transitions, but noticeable abrupt connections\n0.5 points: Frequent abrupt starts and stops between letters\n0 points: No attempt at smooth transitions\nStroke Consistency (2 points)\n2 points: Perfect consistency in height, width, and slant of all strokes\n1.5 points: High consistency with minor variations\n1 point: Moderate consistency with some noticeable variations\n0.5 points: Inconsistent strokes with frequent variations\n0 points: No consistency in stroke execution\n\n\n"""
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_2}"
                    }
                },
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
    "temperature":0.7 
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

response_json = response.json()

# Assuming the relevant content is in 'choices' -> 'message' -> 'content'
calligraphy_output = response_json['choices'][0]['message']['content']

# Print the calligraphy evaluation content
print(calligraphy_output)

second_prompt = f"""Based on the following calligraphy evaluation:\n\n{calligraphy_output}\n\nPlease provide detailed suggestions on how to improve the calligraphy.Here are the factors you can suggest:
Consistent Stroke Pressure
Feedback: Your upstrokes and downstrokes lack contrast.
How to improve:
Use light pressure on upstrokes and heavier pressure on downstrokes to create the necessary contrast.
Practice this by writing basic shapes like lines or loops, focusing on adjusting pressure smoothly.
With a brush or fountain pen, ensure your nib size is appropriate for your desired thickness variation.
Cohesive Strokes
Feedback: The strokes aren't uniform in width and flow.
How to improve:
Focus on building consistent muscle memory by practicing continuous strokes. Slow down if needed, and work in a rhythmic, deliberate manner.
Holding the pen at a consistent angle (around 45 degrees) will help keep your strokes uniform. You can check and correct stroke width by using guidelines to measure consistency.
Smooth Transitions Between Strokes
Feedback: Your transitions between strokes feel abrupt.
How to improve:
Practice drawing curved shapes like ovals or loops to develop fluid motion between strokes.
When moving between upstrokes and downstrokes, ease into the transitions by starting lightly, applying pressure gradually, and then tapering off slowly.
Stroke Consistency
Feedback: Height, width, and slant of strokes vary too much.
How to improve:
Use lined or grid paper to maintain consistent letter size. Focus on the proportions of your strokes (height-to-width ratio) and adjust the slant by keeping the nib and wrist steady.
Practice writing 'a' slowly at first, keeping an eye on each part of the letter and how it fits between the guidelines. Once the shape is consistent, you can gradually increase speed.
Correct Posture and Rhythm
Adjust your posture: Keep your body relaxed yet controlled. A good position helps maintain steady hand movements. Keep your wrist stable but allow your arm to move freely.
Choose the right tool: Make sure your writing instrument feels comfortable in your hand. Experiment with different nib sizes to find the one that provides the right stroke weight.
Develop a rhythm: Focus on keeping a consistent pace as you write, which will help avoid abrupt or jagged movements. Set aside time for slow practice where you emphasize deliberate, flowing lines."""

payload = {
    "model": "gpt-4", 
    "messages": [
        {"role": "system", "content": "You are a calligraphy expert."},
        {"role": "user", "content": second_prompt}
    ],
    "temperature": 0.7  
}

second_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

second_response_json = second_response.json()

suggestions = second_response_json['choices'][0]['message']['content']

print(suggestions)