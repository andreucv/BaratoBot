import telebot
import analyser

token = '250303321:AAEpOPI1RGL_md0ZaLvVvYynDAleeSCXivM'
bot = telebot.TeleBot(token)

def listener(messages):
    for message in messages:
        response, keyboard = analyse(message)
        bot.send_message(message.chat_id, response)

bot.set_update_listener(listener)
bot.polling()

while True: pass
