from config import *
# 
# @bot.message_handler(commands=['start'])
# def starbot(msg):
#     "Ignites the bot application to take action"
#     bot.reply_to(
#         msg, 
#         "Welcome Senior Man to my page.",
#         # reply_markup=menu(msg)
#     )




@server.route('/' + TOKEN, methods=['POST', 'GET'])
def checkWebhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Your bot application is still active!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=SERVER_URL + '/' + TOKEN)
    return "Application running!", 200




if __name__ == "__main__":
    if DEBUG != True:
        server.run(host="0.0.0.0", threaded=True, port=int(os.environ.get('PORT', 5000)))
    else:
        bot.remove_webhook()
        print("Bot polling!")
        bot.polling(none_stop=True)
    # print("Bot Polling!!!!!!")
    # bot.polling(non_stop=True)