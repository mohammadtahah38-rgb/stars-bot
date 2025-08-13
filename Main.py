import os
from telebot import TeleBot

# گرفتن توکن از متغیر محیطی Render
TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

# دستور شروع ربات
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات ستاره فعال شد 🌟")

# دستور تست ستاره دادن (مثال ساده)
@bot.message_handler(commands=['star'])
def star(message):
    bot.reply_to(message, f"{message.from_user.first_name} یک ستاره گرفت ⭐")

bot.polling()
