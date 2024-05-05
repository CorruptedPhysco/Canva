from bs4 import BeautifulSoup
import requests
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route(/)
def home():
  return "home"
