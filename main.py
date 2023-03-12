import datetime
import time

from telebot import TeleBot, types
import constant
import database
import data_quotes

bot = TeleBot(constant.API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    print(message.from_user.first_name)
    database.add_item(message.chat.id, message.from_user.first_name)


def send_text(chat, message):
    bot.send_message(chat, message)


reminder_time = datetime.time(hour=20, minute=52, second=0)

while True:
    # Get the current time
    now = datetime.datetime.now().time()

    # Check if it's time for the daily reminder
    if now.hour == reminder_time.hour and now.minute == reminder_time.minute:
        send_text(database.get_id("Henintsoa"), data_quotes.get_quote())
    time.sleep(60)
