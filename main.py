from bs4 import BeautifulSoup
import requests
from flask import Flask,request,jsonify
from keep_alive import keep_alive
keep_alive()


app = Flask(__name__)

@app.route(/)
def home():
  return "home"
