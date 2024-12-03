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
    С новым днем, снежинка! ❄️✨ Это Ева! Напоминаю, что пришло время заполнить таймшит за вчерашний день. 🎅🎁
    
Пожалуйста, зайди в {link_text} и внеси данные. Это не займет много времени, а для нас это настоящий подарок! 🎁💫
    
Пусть этот день будет волшебным и продуктивным, как у эльфов Санты! 🎄❄️
    """

    evening_message = f"""
    Добрый вечер, снежный герой! 🌟✨ Это снова я, Ева! Напоминаю, что пора заполнить таймшит за сегодняшний день. 🎁🎄
    
Пожалуйста, зайди в {link_text} и внеси данные — это твой маленький вклад в новогоднее волшебство! 🎁💖

Спасибо, что всегда на высоте — ты наша новогодняя звезда! 🌟💖
    """

    current_hour = datetime.datetime.now(moscow_tz).hour
    if current_hour >= 10 and current_hour < 17:
        bot.send_message(CHAT_ID, morning_message, parse_mode="Markdown")
    elif current_hour >= 17:
        bot.send_message(CHAT_ID, evening_message, parse_mode="Markdown")

# Выполнение отправки сообщения
if __name__ == "__main__":
    send_message()