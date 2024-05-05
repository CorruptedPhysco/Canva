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




  url2=job_desc
  page2=requests.get(str(url2))
  html2=page2.content
  soup2 = BeautifulSoup(html2,"html.parser")
  divv = soup2.find(
    'div',class_="col-md-8")
  div = BeautifulSoup(str(divv),"html.parser")
  div22=div.find('div',class_='min-vh-100 d-flex justify-content-center align-items-center')
  div2= BeautifulSoup(str(div22),"html.parser")
  a=div2.find('a',class_="item-wrapper bg-white -outlined text-dark-1 shadow-3")
  hi = str(a)
  li = hi.split()
  b=''
  print(li)
  for i in li:
    if "href" in i:
      b = (i.lstrip('href='))
  g=b.replace('"', '')
  finallink=f'{g}'
  def remove(string):
    return string.replace(" ", "") 
  if "canva" in finallink:
    print('link returned')
    print(remove(finallink))
    return remove(finallink)
  else:
    print('link not returned')
    return 'No'

getlink()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")



bot.polling()
