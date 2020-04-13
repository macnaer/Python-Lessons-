import telebot
from lib.settings import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['about', 'help', 'start'])
def hendler_command(command):
    print("command => ", command)
    if command.text == "/about":
        bot.send_message(
            command.chat.id, "Моніторинг ситуації із кількістю госпіталізованих осіб з підозрою та підтвердженими випадками захворювання на COVID-19")
    elif command.text == "/help" or command.text == "/start":
        bot.send_message(command.chat.id, "Enter country name: ")


@bot.message_handler(content_types=["text"])
def handler_text(message):
    if message.text == "Rome":
        bot.send_message(message.chat.id, "COVID 19 1231 Rome")
    else:
        bot.send_message(message.chat.id, "Use /help for manual")


bot.polling(none_stop=True)
