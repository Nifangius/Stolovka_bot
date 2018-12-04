import telebot
import random 
import json
from telebot import types
import time
from math import *

filename = 'csvjson.json'
with open(filename) as f_obj:
    stolovki = json.load(f_obj)

user_greetings = ['привет','здарова','эщкере','прив','здравствуй','здравствуйте','алоха','хай','hello','хеллоу']
greetings = ["Привет", "Здарова", "Поу-поу-поу",'Бензо Генг!','Здравствуй','Холла']
how_are_you_user = ['как дела','пошел к черту','нет','да','как дела ?','как дела?','боты сасат']
how_are_you = ["Отлично", "Норм", "Расписание на сегодня:\n1.Захватить человечество\n2.Захватить человечество\n3.Покушать\n4.Захватить человечество","Вот результаты теста: ты ужасный человек",'I put A$AP on a tat','Я наполняюсь решительностью']
token = "638760886:AAFtrZqUcjegQzzbsHc6Qig9muY9UIWvGOg" 
bot = telebot.TeleBot(token)

filename = 'csvjson.json'
with open(filename) as f_obj:
    stolovki = json.load(f_obj)
    
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name + ", я найду для тебя места где поесть.\nНапиши пожалуйста радиус поиска в километрах:")
    
@bot.message_handler(content_types=["text"])
def main(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    radius = message.text
    if message.text.lower() in  user_greetings:
        bot.send_message(message.chat.id, random.choice(greetings))
    elif message.text.lower() in how_are_you_user:
        bot.send_message(message.chat.id, random.choice(how_are_you))
    else:
        if float(radius) > 0 and float(radius) < 10:
            bot.send_message(message.chat.id,'Спасибо, а теперь отправь своё местоположение', reply_markup=keyboard)
    @bot.message_handler(content_types=["location"])
    def read_location_data(message):
        for item in stolovki:
            a = haversine(float(item['latitude']),float(item['longitude']),message.location.latitude,message.location.longitude)
        if a < float(radius) :
            bot.send_message(message.chat.id, item['Наименование объекта общественного питания'] +'\n Адрес: '+ item['address'] + '\n Рейтинг: '+ str(item['Оценка']))
    
def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2)** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km





if __name__ == "__main__":
    bot.polling(none_stop=True)




