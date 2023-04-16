# from google_sheets.celery import app
import telebot
from django.conf import settings
import requests
import time

# TOKEN: '5603456251:AAER2H_ALwag2opjfE9yN2lJSRTiA5VhgIU' stored in settings.TELEGRAM_BOT_TOKEN
# CHAT ID: 5218003772 stored in settings.TELEGRAM_CHAT_ID


# @app.task
def msg_to_telegram(message):
    chat_ids = [5282220678, 5218003772]
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    for chat_id in chat_ids:
        bot.send_message(chat_id, message)
        time.sleep(1)


def msg_to_channel(message):
    apiURL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    print(apiURL)
    try:
        response = requests.post(apiURL, json={'chat_id': 5282220678, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
