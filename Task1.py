#Задача №1________________________________________________

import telebot
import re

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте!\nЭто Бот-калькулятор. Введите выражени, которое хотите вычислить.\nНапример: 1+2*3")
        
@bot.message_handler(content_types=['text'])
def calculator(messege):
    if re.search('\d+', messege.text) is not None:
        bot.reply_to(messege,eval(messege.text))
    else:
        bot.reply_to(messege, 'Введите пожалуйста цифры.')

bot.infinity_polling()
