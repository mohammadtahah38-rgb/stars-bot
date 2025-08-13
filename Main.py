import os
from telebot import TeleBot

TOKEN = os.getenv("8301827690:AAG62x2naz4okPNVf9-Z6xmXZAxPN4F7B9U")
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات ستاره فعال شد 🌟")

bot.polling()
