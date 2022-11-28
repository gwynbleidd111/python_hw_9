#Задача №2________________________________________________

import random
import telebot

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, f'Я загадал число от 1 до 10. Ваша задача угадать это число.\nСыграем?')
    
@bot.message_handler(content_types=['text'])
def game(message):
    user_text = message.text
    if message.text == 'да':
        global random_game
        random_game = random.randint(1,1000)
        bot.reply_to(message, 'Введите число.')
        print(random_game)
        global count
        count = 0
    else:
        if not user_text.isdigit():
            msg = bot.reply_to(message, 'Введите пожалуйста цифры.')
            bot.register_next_step_handler(msg, game)
            count -=1
        else:
            if random_game != int(user_text):
                bot.reply_to(message, 'Неверно. Давайте еще раз.')
            else:
                if random_game == int(user_text):
                    bot.reply_to(message, f'Ура! Вы угадали с {count} попытки.')
    count +=1


bot.infinity_polling()
