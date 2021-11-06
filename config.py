from flask import Flask, request
import telebot 
import os

# https://fathomless-cove-36805.herokuapp.com/ | https://git.heroku.com/fathomless-cove-36805.git


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )



admin = 1190069449
TOKEN = "2093122663:AAEm1zqmeiz8pUPgyvWrHG62Vj2FbF9tYRw"


DEBUG = True

SERVER_URL = 'https://fathomless-cove-36805.herokuapp.com'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


import importdir
importdir.do("main", globals())
