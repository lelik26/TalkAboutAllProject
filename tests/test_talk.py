from unittest.mock import Mock, patch

import pytest
from telegram import Update, Message
from telegram.ext import CallbackContext

from services.talk_about_all import talk_with_assistant


@pytest.fixture
def mock_openai():
    with patch('services.talk_about_all.openai.OpenAI') as mock:
        yield mock


# Тест успешного ответа
def test_successful_response(mock_openai):
    mock_client = Mock()
    mock_openai.return_value = mock_client

    # Мокируем ответ API
    mock_client.beta.threads.create.return_value = Mock(id="thread_123")
    mock_client.beta.threads.runs.create_and_poll.return_value = Mock(status="completed")
    mock_client.beta.threads.messages.list.return_value = Mock(data=[
        Mock(role="assistant", content=[Mock(text=Mock(value="Test response"))])
    ])

    response = talk_with_assistant("Hello")
    assert response == "Test response"


# Тест ошибки API
def test_api_error(mock_openai):
    mock_client = Mock()
    mock_openai.return_value = mock_client
    mock_client.beta.threads.create.side_effect = Exception("API Error")

    response = talk_with_assistant("Hello")
    assert "внутренняя ошибка" in response


# Асинхронный тест обработчика
@pytest.mark.asyncio
async def test_talk_handler():
    from handlers.talk_handlers import talk_response

    update = Mock(Update)
    update.message = Mock(Message)
    update.message.text = "Test message"
    context = Mock(CallbackContext)

    with patch('handlers.talk_handlers.asyncio.to_thread') as mock_thread:
        mock_thread.return_value = "Mocked response"
        await talk_response(update, context)
        update.message.reply_text.assert_called_with("Mocked response")