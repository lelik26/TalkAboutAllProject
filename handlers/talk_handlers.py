from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import setup_logger
from services.talk_about_all import talk_with_assistant
import asyncio

logger = setup_logger(__name__)

async def talk_command(update: Update, _: CallbackContext) -> None:
    try:
        await update.message.reply_text("👌Можем поговорить на любые темы 💡Напиши мне что-нибудь 📍, и я отвечу 💬:")
    except Exception as e:
        logger.error(f"Ошибка в talk_command: {str(e)}")

async def talk_response(update: Update, context: CallbackContext) -> None:
    try:
        user_message = update.message.text

        # Показываем индикатор "печатает"
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

        # Добавляем небольшую задержку, чтобы индикатор успел отобразиться
        await asyncio.sleep(2)

        # Получаем ответ от ассистента
        response = await asyncio.to_thread(talk_with_assistant, user_message)

        # Отправляем ответ пользователю
        await update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Ошибка обработки сообщения: {str(e)}")
        await update.message.reply_text("⚠️ Произошла ошибка. Попробуйте позже.")