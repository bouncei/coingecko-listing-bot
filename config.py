from flask import Flask, request
import telebot 
import os

# https://cryptic-beyond-34140.herokuapp.com/ | https://git.heroku.com/cryptic-beyond-34140.git


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )



admin = 1190069449
TOKEN = "2093122663:AAEm1zqmeiz8pUPgyvWrHG62Vj2FbF9tYRw"


DEBUG = True

SERVER_URL = 'https://cryptic-beyond-34140.herokuapp.com'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


import importdir
importdir.do("main", globals())
