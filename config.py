from flask import Flask, request
import flask
import telebot 
import os
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException, Timeout
from requests.sessions import TooManyRedirects, session 
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import schedule


load_dotenv()
# https://sleepy-chamber-23428.herokuapp.com/ | https://git.heroku.com/sleepy-chamber-23428.git

# Webpage_url = "https://www.coingecko.com/it/monete/recently_added"
# coin_url = 'https://api.coingecko.com/api/v3/coins/list'

# recently_added = ''



# old_name = ''

GROUP = -1001619147060



# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )



ADMIN = os.getenv('ADMIN')
TOKEN = os.getenv('TOKEN')

admin = 1190069449

DEBUG = False

SERVER_URL = 'https://sleepy-chamber-23428.herokuapp.com'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


import importdir
importdir.do("main", globals())
