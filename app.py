import os
import asyncio
from datetime import datetime

print("Начало загрузки модулей...")

try:
    import pandas as pd
    print("✓ pandas загружен")
except Exception as e:
    print(f"✗ Ошибка pandas: {e}")

try:
    from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
    print("✓ telegram загружен")
except Exception as e:
    print(f"✗ Ошибка telegram: {e}")

try:
    from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
    print("✓ telegram.ext загружен")
except Exception as e:
    print(f"✗ Ошибка telegram.ext: {e}")

try:
    from flask import Flask
    print("✓ flask загружен")
except Exception as e:
    print(f"✗ Ошибка flask: {e}")

print("Все модули проверены!")
print(f"BOT_TOKEN задан: {bool(os.environ.get('BOT_TOKEN'))}")
print(f"ADMIN_ID задан: {bool(os.environ.get('ADMIN_ID'))}")

# Короткий тест создания приложения
try:
    from telegram.ext import Application
    bot_token = os.environ.get('BOT_TOKEN', 'test')
    app = Application.builder().token(bot_token).build()
    print("✓ Application создан успешно")
except Exception as e:
    print(f"✗ Ошибка создания Application: {e}")

print("Скрипт завершил работу")

# Запуск Flask для поддержки порта
if __name__ == "__main__":
    from flask import Flask
    flask_app = Flask(__name__)
    
    @flask_app.route('/')
    def home():
        return "Bot is running (test mode)"
    
    port = int(os.environ.get("PORT", 5000))
    print(f"Запуск Flask на порту {port}...")
    flask_app.run(host="0.0.0.0", port=port)
