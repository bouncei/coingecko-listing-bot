from config import *


Webpage_url = "https://www.coingecko.com/it/monete/recently_added"
coin_url = 'https://api.coingecko.com/api/v3/coins/list'

recently_added = ''
# old_name = 'BabyFlokiZilla'
old_name = ''

def get_coin(web, api):
    global recently_added
    global old_name

    request_timeout = 120

    session = requests.session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    try:

        Webpage_url_response = session.get(web)
        coin_url_response = session.get(api, timeout=request_timeout).json() 

        coin_gecko_webpage = "https://www.coingecko.com/en/coins/" 



        for line in Webpage_url_response.text.splitlines():
            if '<td class="py-0 coin-name" data-sort=' in line:
                name = line[len('<td class="py-0 coin-name" data-sort=')+1:-2]
                
                if name == old_name:
                    print("Coingecko has not added a anything yet")
                    recently_added = ''
                    break

                else:
                    old_name = name
                    for coin in coin_url_response:
                        if coin['name'] == name:
                            recently_added = coin_gecko_webpage + coin['id']
                            new_coin = requests.get("https://api.coingecko.com/api/v3/coins/" + coin['id']).json()
                            print(new_coin['name'], new_coin['id'], new_coin['symbol'])   ## Displays the details of the newly listed coin from coingecko in the command line
                            


                print(f"The new name is {old_name}")
                break

            

            # else:
                # print("Baba omo I no see any coin")  # Pycomet, I'm so sorry that you had to read this line of code 😂

    # Check for posiible exception errors
    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(e)


    # print(recently_added)
    return recently_added



                


if get_coin(Webpage_url, coin_url):
    schedule.every(10).seconds.do(get_coin, Webpage_url, coin_url)
    c_message = f"{old_name} has just been added to CoinGecko. {recently_added}"
    bot.send_message(ADMIN, c_message)

    while True:       
        schedule.run_pending()
        time.sleep(1)



# print(recently_added, old_name)




# @bot.message_handler





