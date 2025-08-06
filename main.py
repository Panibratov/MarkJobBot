import os
from datetime import datetime
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = Bot(token=TOKEN)

def fetch_jobs():
    now = datetime.now().strftime("%d %b %Y %H:%M")
    text = f"✅ Тестовое сообщение от Job Bot\nДата: {now}\nРаботаем!"
    bot.send_message(chat_id=CHANNEL_ID, text=text)

scheduler = BlockingScheduler()
scheduler.add_job(fetch_jobs, 'cron', hour='9,13,19', minute=0)

fetch_jobs()
print("⏳ Бот запущен. Ждём расписания...")
scheduler.start()
