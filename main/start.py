from function import *

if get_coin(Webpage_url, coin_url):
    schedule.every(5).minutes.do(get_coin, Webpage_url, coin_url)
    c_message = f"{old_name} has just been added to CoinGecko. {recently_added}"
    bot.send_message(str(GROUP), c_message)

    while True:       
        schedule.run_pending()
        time.sleep(1)










# @bot.message_handler(commands=['help'])
# def starbot(msg):
#     "Ignites the bot application to take action"
#     bot.reply_to(
#         msg, 
#         "Welcome, do You need help Senior Man.",
#         # reply_markup=menu(msg)
#     )



# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def echo_message(message):
#     bot.reply_to(message, message.text)





# if get_coin(Webpage_url, coin_url):
#     schedule.every(180).seconds.do(get_coin, Webpage_url, coin_url)
#     c_message = f"{old_name} has just been added to CoinGecko. {recently_added}"
#     bot.send_message(ADMIN, c_message)

#     while True:       
#         schedule.run_pending()
#         time.sleep(1)



