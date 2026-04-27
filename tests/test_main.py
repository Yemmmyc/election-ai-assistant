import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")

def test_chat_empty_message():
    response = client.post("/chat", json={"message": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Message cannot be empty"

def test_chat_valid_message(monkeypatch):
    # Mock ask_ai so we don't actually hit the Gemini API during tests
    def mock_ask_ai(prompt, session_id):
        return "This is a mock AI response for testing."
    
    # We patch ask_ai inside app.main
    monkeypatch.setattr("app.main.ask_ai", mock_ask_ai)
    
    response = client.post("/chat", json={"message": "When is the next election?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["response"] == "This is a mock AI response for testing."
    assert "session_id" in data
