import os
import telebot
import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

def send_message():
    moscow_tz = pytz.timezone('Europe/Moscow')

    resource_url = "https://crm-1c-resource.phoenixit.ru/"
    link_text = "[Ресурс]({})".format(resource_url)

    morning_message = f"""
    Доброе утро! 😊 Это Ева. Напоминаю, что пришло время заполнить таймшит за вчерашний день! 
    
Пожалуйста, зайди в {link_text} и внеси данные. Это не займет много времени, а нам очень важно! 📝✨
    
Пусть этот день будет продуктивным и успешным! 🌞
    """

    evening_message = f"""
    Приветик! 😇 Это снова я, Ева! Напоминаю, что пришло время заполнить таймшит за сегодняшний день. 
    
Пожалуйста, зайди в {link_text} и внеси данные. Это не займет много времени, а нам очень важно! 📝✨

Ты классный, спасибо, что не забываешь! 💖
    """

    current_hour = datetime.datetime.now(moscow_tz).hour
    if current_hour >= 10 and current_hour < 17:
        bot.send_message(CHAT_ID, morning_message, parse_mode="Markdown")
    elif current_hour >= 17:
        bot.send_message(CHAT_ID, evening_message, parse_mode="Markdown")

# Выполнение отправки сообщения
if __name__ == "__main__":
    send_message()