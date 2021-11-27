from config import *




recently_added = ''
old_name = ''

def menu(address):
    """ Redirects User to poocoin chart"""

    keyboard = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton(text="POOCOIN", url="https://poocoin.app/tokens/" + address)
    b = types.InlineKeyboardButton(text="POOCOIN", url="https://bscscan.com/tokens/" + address)
      

    keyboard.row(a,b)

    return keyboard



def get_address(name):
    """Gets The contact address of the recently added coin """
    request_timeout = 120

    session = requests.session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    
    try:
        page_response = session.get(f"https://www.coingecko.com/en/coins/{name}")

        for line in page_response.text.splitlines():
            if '<i data-address="0' in line:
                address = line[len('<i data-address=')+1: len('<i data-address=')+43]
                print("The contact address is: ", address)
                

            else:
                pass

        


    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(e)

    return address
    


scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", minutes=2)
def get_coin():
    global recently_added
    global old_name
    Webpage_url = "https://www.coingecko.com/it/monete/recently_added"
    coin_url = 'https://api.coingecko.com/api/v3/coins/list'




    web = Webpage_url
    api = coin_url



    request_timeout = 120

    session = requests.session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    try:

        Webpage_url_response = session.get(web)
        coin_url_response = session.get(api, timeout=request_timeout).json() 
        # time.sleep(10)

        coin_gecko_webpage = "https://www.coingecko.com/en/coins/" 



        for line in Webpage_url_response.text.splitlines():
            if '<td class="py-0 coin-name" data-sort=' in line:
                name = line[len('<td class="py-0 coin-name" data-sort=')+1:-2]
                
                if name == old_name:
                    print("Coingecko has not added anything yet")
                    recently_added = ''

                    
                    break

                else:
                    old_name = name
                    print(f"The new name is {old_name}")
                    for coin in coin_url_response:
                        if coin['name'] == name:
                            coin_id = coin['id']               ## Gets coin id
                            recently_added = coin_gecko_webpage + coin['id']
                            new_coin = requests.get("https://api.coingecko.com/api/v3/coins/" + coin['id']).json()
                            print(new_coin['name'], new_coin['id'], new_coin['symbol'])   ## Displays the details of the newly listed coin from coingecko in the command line
                            
                    break

                
                

            

            # else:
                # print("Baba omo I no see any coin")  # Pycomet, I'm so sorry that you had to read this line of code 😂

    # Check for posiible exception errors
    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(e)

    print(recently_added)

    if recently_added != '':
        contract_address = get_address(coin_id)
        right_now = datetime.time(datetime.now())
        formatted_time = str(right_now)[:8]

        

        bot.send_message(
            str(GROUP),
            f"""
🟢[{old_name}] {coin_id}

<b>Coin name: </b>  <a>{old_name}</a>
<b>Address: </b>      {contract_address}

<b>Time:   </b>         {formatted_time} UTC




            """,

            parse_mode="html",
            reply_markup=menu(contract_address) 
            
        )
    
    else:
        print("no new coin boss")
        


   











scheduler.start()



# def send_coin():
#     if get_coin() == old_name:
#         print("Coingecko has not added anything yet")

#     else:
#         old_name = get_coin()
#         print(f"The new name is {old_name}")
#         for coin in coin_url_response:
#             if coin['name'] == name:
#                 recently_added = coin_gecko_webpage + coin['id']
#                 new_coin = requests.get("https://api.coingecko.com/api/v3/coins/" + coin['id']).json()
#                 print(new_coin['name'], new_coin['id'], new_coin['symbol'])   ## Displays the details of the newly listed coin from coingecko in the command line

#     return recently_added













