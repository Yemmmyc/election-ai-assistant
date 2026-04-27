import pytest
from unittest.mock import patch, MagicMock
from app.ai import ask_ai, chat_sessions

@pytest.fixture(autouse=True)
def clear_chat_sessions():
    """Clear in-memory chat sessions before each test."""
    chat_sessions.clear()

@patch("app.ai.genai.GenerativeModel")
def test_ask_ai_success(mock_model_class):
    # Setup mock
    mock_model_instance = MagicMock()
    mock_chat_session = MagicMock()
    mock_response = MagicMock()
    
    mock_response.text = "This is a successful response."
    mock_chat_session.send_message.return_value = mock_response
    mock_model_instance.start_chat.return_value = mock_chat_session
    mock_model_class.return_value = mock_model_instance
    
    response = ask_ai("When is the election?", "session_123")
    
    assert response == "This is a successful response."
    mock_model_class.assert_called_once()
    mock_model_instance.start_chat.assert_called_once()
    mock_chat_session.send_message.assert_called_with("When is the election?")
    assert "session_123" in chat_sessions

@patch("app.ai.genai.GenerativeModel")
def test_ask_ai_empty_response(mock_model_class):
    mock_model_instance = MagicMock()
    mock_chat_session = MagicMock()
    mock_response = MagicMock()
    
    mock_response.text = ""
    mock_chat_session.send_message.return_value = mock_response
    mock_model_instance.start_chat.return_value = mock_chat_session
    mock_model_class.return_value = mock_model_instance
    
    response = ask_ai("Hello", "session_empty")
    
    assert response == "I'm sorry, I couldn't generate a response. Please try asking in a different way."

@patch("app.ai.genai.GenerativeModel")
@patch("app.ai.time.sleep")
def test_ask_ai_retry_logic_then_success(mock_sleep, mock_model_class):
    mock_model_instance = MagicMock()
    mock_chat_session = MagicMock()
    mock_response = MagicMock()
    
    mock_response.text = "Success after retry!"
    
    # First call raises an exception (e.g., 503 UNAVAILABLE), second call succeeds
    mock_chat_session.send_message.side_effect = [
        Exception("503 UNAVAILABLE"),
        mock_response
    ]
    
    mock_model_instance.start_chat.return_value = mock_chat_session
    mock_model_class.return_value = mock_model_instance
    
    response = ask_ai("Retry test", "session_retry")
    
    assert response == "Success after retry!"
    assert mock_chat_session.send_message.call_count == 2
    mock_sleep.assert_called_once_with(1)

@patch("app.ai.genai.GenerativeModel")
@patch("app.ai.time.sleep")
def test_ask_ai_quota_exhausted(mock_sleep, mock_model_class):
    mock_model_instance = MagicMock()
    mock_chat_session = MagicMock()
    
    # All 3 calls fail with 429
    mock_chat_session.send_message.side_effect = [
        Exception("429 RESOURCE_EXHAUSTED"),
        Exception("429 RESOURCE_EXHAUSTED"),
        Exception("429 RESOURCE_EXHAUSTED")
    ]
    
    mock_model_instance.start_chat.return_value = mock_chat_session
    mock_model_class.return_value = mock_model_instance
    
    response = ask_ai("Quota test", "session_quota")
    
    assert response == "The AI is currently receiving too many requests due to quota limits. Please try again in a minute."
    assert mock_chat_session.send_message.call_count == 3
    assert mock_sleep.call_count == 2

@patch("app.ai.genai.GenerativeModel")
def test_ask_ai_api_key_error(mock_model_class):
    mock_model_instance = MagicMock()
    mock_chat_session = MagicMock()
    
    # Fails with API_KEY error immediately (no retry expected for API_KEY errors)
    mock_chat_session.send_message.side_effect = Exception("API_KEY invalid")
    
    mock_model_instance.start_chat.return_value = mock_chat_session
    mock_model_class.return_value = mock_model_instance
    
    response = ask_ai("Auth test", "session_auth")
    
    assert response == "There is an issue with the API authentication. Please ensure the API key is set correctly."
    assert mock_chat_session.send_message.call_count == 1
