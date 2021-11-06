from flask import Flask, request
import telebot 
import os

# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )



admin = ""
TOKEN = "2093122663:AAEm1zqmeiz8pUPgyvWrHG62Vj2FbF9tYRw"


DEBUG = True

SERVER_URL = ""

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
