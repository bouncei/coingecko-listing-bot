import requests
from requests.exceptions import RequestException, Timeout
from requests.sessions import TooManyRedirects, session 
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


Webpage_url = "https://www.coingecko.com/it/monete/recently_added"
coin_url = 'https://api.coingecko.com/api/v3/coins/list'



def get_coin(web, api):
    request_timeout = 120

    session = requests.session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))

    try:

        Webpage_url_response = session.get(web)
        coin_url_response = session.get(api, timeout=request_timeout).json()  



        for line in Webpage_url_response.text.splitlines():
            if '<td class="py-0 coin-name" data-sort=' in line:
                name = line[len('<td class="py-0 coin-name" data-sort=')+1:-2]
                print(f"This name of the coin is: {name}")   ## Displays the name of the new coin

                for coin in coin_url_response:
                    if coin['name'] == name:
                        new_coin = requests.get("https://api.coingecko.com/api/v3/coins/" + coin['id']).json()
                        print(new_coin['name'], new_coin['symbol'])   ## Displays the details of the newly listed coin from coingecko in the command line


            # else:
                # print("Baba omo I no see any coin")  # Pycomet, I'm so sorry that you had to read this line of code 😂

    # Check for posiible exception errors
    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(e)
                

get_coin(Webpage_url, coin_url)