import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

models_to_test = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro",
    "gemini-2.5-flash",
    "gemini-pro",
]

client = genai.Client()

for model in models_to_test:
    print(f"Testing {model}...")
    try:
        response = client.models.generate_content(
            model=model,
            contents="say hello",
        )
        print(f"SUCCESS with {model}: {response.text}")
    except Exception as e:
        print(f"FAILED {model}: {str(e)}")
