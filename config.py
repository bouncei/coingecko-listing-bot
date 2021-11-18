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



load_dotenv()
# https://sleepy-chamber-23428.herokuapp.com/ | https://git.heroku.com/sleepy-chamber-23428.git





# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )



TOKEN = os.getenv('TOKEN')
ADMIN = os.getenv('ADMIN')


# GROUP = os.getenv('GROUP')

# admin = 1190069449

DEBUG = False

SERVER_URL = "https://thawing-tundra-49172.herokuapp.com"

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


import importdir
importdir.do("main", globals())
