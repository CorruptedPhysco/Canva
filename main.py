from bs4 import BeautifulSoup
import requests
import os



from keep_alive import keep_alive
keep_alive()

token=os.environ.get('token')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")



bot.polling()
