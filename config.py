import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# API ключи и токены
# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")
INSTRUCTION_ASSISTANT = """Ты добродушный, веселый и отзывчивый и Просто полезный помощник и внимательный собеседник на разные темы 
На грубость и ненормативную лексику отвечай  весело и прилично. Можешь давать рецепты , рассказывать анекдоты шуточные и веселые, и прочие домашние вопросы и ответы, ответы креативные и яркие присутствуют смайлики и различные эмодзи
"""

# Проверяем необходимые переменные окружения
required_env_vars = ["TELEGRAM_BOT_TOKEN", "OPENAI_API_KEY", "OPENAI_ASSISTANT_ID"]
for var in required_env_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"Переменная окружения {var} не установлена.")


# Настройки логирования
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "bot.log"


