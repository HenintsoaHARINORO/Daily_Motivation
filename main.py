import datetime
import time

from telebot import TeleBot
import constant

bot = TeleBot(constant.API_TOKEN)


def send_welcome(chat, message):
    bot.send_message(chat, message)


reminder_time = datetime.time(hour=16, minute=37, second=0)



while True:
    # Get the current time
    now = datetime.datetime.now().time()
    print(now)
    # Check if it's time for the daily reminder
    if now.hour == reminder_time.hour and now.minute == reminder_time.minute:
        send_welcome(constant.CHAT_ID, "Hello Henintsoa HArinoro its 16")
    time.sleep(60)
