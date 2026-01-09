import telebot
import time
from threading import Thread
from flask import Flask

# خادم وهمي لإرضاء Render
app = Flask('')
@app.route('/')
def home(): return "Bot is Running"
def run_web(): app.run(host='0.0.0.0', port=8080)

# إعدادات البوت
TOKEN = "8055591248:AAH13-YdwNMDcKEh7szqwKJhaXDio27pjCs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ أهلاً بك! البوت يعمل الآن بنجاح على سيرفر Render.")

def run_bot():
    print("البوت بدأ العمل...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"خطأ: {e}")
            time.sleep(5)

if __name__ == "__main__":
    Thread(target=run_web).start()
    run_bot()
