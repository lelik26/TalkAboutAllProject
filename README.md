# Проект:  Поговорить обо всём (Talk about all)


## 📌 О проекте

**Talk about all** — это интеллектуальный чат-бот для разговоров с пользователем на бытовые темы обо всём

## 🚀 Функционал

- 🔹 **Генерация  текстов** языков с помощью OpenAI API.
- 🔹 **Гибкая настройка команд** через TelegramBot API.

## 🛠️ Технологии

- **Язык программирования:** Python 3.12
- **Библиотеки:**
  - python-telegram-bot — для взаимодействия с Telegram API
  - `dotenv` — для безопасного хранения API-ключей
  - `Open API` — для генерации текста
  - `ElevenLabs API` — для озвучивания

## 📂 Структура проекта

```
TeacherLearningLanguagesBot/
│── main.py                # Основной файл бота
│── config.py             # Конфигурация и загрузка API-ключей
│── handlers/             # Обработчики команд
│── services/             # Логика перевода и озвучивания
│── .env                  # Переменные окружения (не загружать в репозиторий!)
│── requirements.txt      # Список зависимостей
│── README.md             # Документация проекта
```

## 🔧 Установка и запуск

1. **Склонируйте репозиторий:**
   ```sh
   git clone 
   cd 
   ```
2. **Создайте виртуальное окружение и установите зависимости:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. **Создайте файл ************************************`.env`************************************ и добавьте API-ключи:**
   ```ini
   TELEGRAM_BOT_TOKEN=your_telegram_token
   OPENAI_API_KEY=your_openai_api_key
  
   ```
4. **Запустите бота:**
   ```sh
   python main.py
   ```

## 📜 Лицензия

Проект распространяется под лицензией MIT.

---

**Автор:** lelik26


