import requests
import json

url = "https://api.coingecko.com/api/v3/coins/list?include_platform=false&__cf_chl_captcha_tk__=6jDayb2TozA.DjxN5TDp2F.c5BaE7XThkX9CjpEcLcw-1636355162-0-gaNycGzNCb0"

re = requests.get(url).status_code
print(re)

# j = json.loads(re)
# print(j)

