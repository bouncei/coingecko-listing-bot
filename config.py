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
TOKEN = ""
DEBUG = True

SERVER_URL = ""

bot = telebot.Telebot(TOKEN)
server = Flask(__name__)
