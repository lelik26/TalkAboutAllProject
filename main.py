import asyncio
from telegram import BotCommand, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import config as cfg
from handlers.talk_handlers import talk_command, talk_response
from utils.logger import setup_logger

logger = setup_logger(__name__)

class TalkAboutAllBot:
    def __init__(self):
        """Инициализирует бота и необходимые компоненты."""
        self.app = Application.builder().token(cfg.TELEGRAM_BOT_TOKEN).build()

    def setup_handlers(self):
        """Настраивает обработчики команд и сообщений бота."""
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("talk", talk_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_response))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Обрабатывает команду /start."""
        welcome_text = (
            "👋 Привет, меня зовут 👩‍🦰Болтушка! Я могу болтать на любые бытовые темы! Ты пишешь ✏️мне - я отвечаю 💬.\n\n"
            "Используй команды, чтобы поболтать со мной:\n\n"
            "💬 /talk - Поболтать обо всём.\n\n\n"
            "ℹ️ /help - помощь."
        )
        await update.message.reply_text(welcome_text)
        logger.info(f"Пользователь {update.effective_user.id} начал работу с ботом.")

    async def help_command(self, update: Update, context: CallbackContext):
        """Отправляет пользователю список команд и информацию о поддержке."""
        help_text = (
            "ℹ️ **Помощь**\n\n"
            "🥳Я могу болтать на любые бытовые темы!:\n\n"
            "💬 /talk - Поболтать обо всём.\n\n\n"
            "ℹ️ /help - помощь и связь с поддержкой.\n\n"
            "💬 **Связаться с поддержкой**: [Написать в поддержку](https://t.me/i_VAN_79)"
        )
        await update.message.reply_text(help_text, parse_mode="Markdown", disable_web_page_preview=True)

    async def set_bot_commands(self):
        """Устанавливает команды для быстрого выбора в Telegram."""
        commands = [
            BotCommand("start", "Запустить бота"),
            BotCommand("talk", "Поболтать обо всём"),
            BotCommand("help", "Помощь и техподдержка")
        ]
        tg_bot = self.app.bot if self.app.bot else await self.app.get_bot()
        await tg_bot.set_my_commands(commands)
        logger.info("Команды бота установлены.")

async def main():
    bot = TalkAboutAllBot()
    bot.setup_handlers()
    await bot.app.initialize()         # Инициализация приложения
    await bot.set_bot_commands()       # Установка команд
    await bot.app.start()              # Запуск приложения
    await bot.app.updater.start_polling()  # Запуск polling
    logger.info("Бот запущен и готов к работе.")
    # Блокируем выполнение, чтобы бот работал бесконечно
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        await bot.app.stop()

if __name__ == "__main__":
    asyncio.run(main())