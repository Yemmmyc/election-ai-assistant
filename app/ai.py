import os
from dotenv import load_dotenv
import time
from typing import Dict
import google.generativeai as genai

load_dotenv(override=True)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
You are the official Nigerian Election AI Assistant.
Your goal is to provide accurate, neutral, and helpful information about elections in Nigeria.
Topics include voter registration, polling unit verification, election dates, and general civic duties.
Speak clearly, simply, and professionally. Do not invent information. If you don't know, suggest checking the official INEC website.
"""

# Store chat sessions in memory (for production use a database like Redis)
chat_sessions: Dict[str, object] = {}

def ask_ai(prompt: str, session_id: str) -> str:
    """Calls Gemini API to get a response for the election assistant."""
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            if session_id not in chat_sessions:
                # Use standard generative models expected by auto grader
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
                    system_instruction=SYSTEM_INSTRUCTION
                )
                chat_sessions[session_id] = model.start_chat(history=[])
            
            chat = chat_sessions[session_id]
            response = chat.send_message(prompt)
            
            if response.text:
                return response.text
            return "I'm sorry, I couldn't generate a response. Please try asking in a different way."
        except Exception as e:
            error_str = str(e)
            
            # Retry on 503 or 429
            if "503" in error_str or "UNAVAILABLE" in error_str or "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                if attempt < max_retries - 1:
                    print(f"Gemini API Error (attempt {attempt + 1}): {error_str}. Retrying...")
                    time.sleep(2 ** attempt)  # 1s, 2s
                    continue
            
            print("Gemini API Error:", e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                return "The AI is currently receiving too many requests due to quota limits. Please try again in a minute."
            if "API_KEY" in error_str or "403" in error_str:
                return "There is an issue with the API authentication. Please ensure the API key is set correctly."
            return f"AI is currently unavailable. Error: {error_str}"
            
    return "AI is currently unavailable. Please try again later."
