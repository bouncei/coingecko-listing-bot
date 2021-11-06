from config import *


@bot.message_handler(commands=['start'])
def starbot(msg):
    "Ignites the bot application to take action"

    if msg.user_id != admin:
        bot.reply_to(msg, "Unauthorized Userr!!")

    else:

        bot.reply_to(
            msg, 
            f"This is a userBot customized for {msg.username} to recieve coin listing from coingecko API",
            # reply_markup=menu(msg)
        )

    



@bot.message_handler(commands=['help'])
def starbot(msg):
    "Ignites the bot application to take action"
    bot.reply_to(
        msg, 
        "Welcome, do You need help Senior Man.",
        # reply_markup=menu(msg)
    )



@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
