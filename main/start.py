from config import *

@bot.message_handler(commands=['start', 'help'])
def starbot(msg):
    "Ignites the bot application to take action"
    bot.reply_to(
        msg, 
        "Welcome Senior Man to my page.",
        # reply_markup=menu(msg)
    )


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
