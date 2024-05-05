from flask import Flask,render_template
import requests 
from bs4 import BeautifulSoup
from threading import Thread

app = Flask(__name__)



def getlink():
  url="https://bingotingo.com/best-social-media-platforms/"
  page=requests.get(url)
  html=page.content
  soup = BeautifulSoup(html,"html.parser") 
  job_desc = soup.find(
    'a', 
    class_='su-button su-button-style-soft su-button-wide')
  l = str(job_desc)
  list = l.split()
  for i in list:
    if "href" in i:
      j = (i.lstrip('href='))
      job_desc=j.replace('"', '')
  return job_desc
 
@app.route('/')
def index():
  return getlink()


def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t=Thread(target=run)
  t.start()
