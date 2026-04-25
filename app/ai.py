import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

SYSTEM_INSTRUCTION = """
You are the official Nigerian Election AI Assistant.
Your goal is to provide accurate, neutral, and helpful information about elections in Nigeria.
Topics include voter registration, polling unit verification, election dates, and general civic duties.
Speak clearly, simply, and professionally. Do not invent information. If you don't know, suggest checking the official INEC website.
"""

def ask_ai(prompt: str) -> str:
    """Calls Gemini API to get a response for the election assistant."""
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )
        if response.text:
            return response.text
        return "I'm sorry, I couldn't generate a response. Please try asking in a different way."
    except Exception as e:
        print("Gemini API Error:", e)
        error_str = str(e)
        if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
            return "The AI is currently receiving too many requests due to quota limits. Please try again in a minute."
        if "API_KEY" in error_str or "403" in error_str:
            return "There is an issue with the API authentication. Please ensure the API key is set correctly."
        return f"AI is currently unavailable. Error: {error_str}"
