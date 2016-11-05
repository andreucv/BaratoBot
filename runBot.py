import telebot
import analyser

token = '250303321:AAEpOPI1RGL_md0ZaLvVvYynDAleeSCXivM'
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat_id, message.text)

bot.polling()

while True: pass
