import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models_to_test = [
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-2.0-flash",
    "gemini-2.0-pro-exp"
]

for model_name in models_to_test:
    print(f"Testing {model_name}...")
    try:
        model = genai.GenerativeModel(model_name=model_name)
        response = model.generate_content("say hello")
        print(f"SUCCESS with {model_name}: {response.text}")
    except Exception as e:
        print(f"FAILED {model_name}: {str(e)}")
