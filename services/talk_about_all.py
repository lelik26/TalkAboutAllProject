import openai
from utils.logger import setup_logger
import config as cfg
from typing import Optional

logger = setup_logger(__name__)

client = openai.OpenAI(api_key=cfg.OPENAI_API_KEY)


def talk_with_assistant(user_message: str) -> Optional[str]:
    try:
        if not user_message or len(user_message) > 2000:
            raise ValueError("Некорректный запрос")

        thread = client.beta.threads.create()
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=cfg.ASSISTANT_ID,
            instructions=cfg.INSTRUCTION_ASSISTANT
        )

        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            assistant_messages = [msg for msg in messages.data if msg.role == "assistant"]
            return assistant_messages[-1].content[0].text.value if assistant_messages else "Ответ не найден"

        return f"Статус обработки: {run.status}"

    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        return "Произошла внутренняя ошибка. Попробуйте снова."