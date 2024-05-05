from bs4 import BeautifulSoup
import requests
import os
import telebot


from keep_alive import keep_alive
keep_alive()

token=os.environ.get('token')
bot = telebot.TeleBot(token)




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
      print(job_desc)
 


getlink()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")



bot.polling()
