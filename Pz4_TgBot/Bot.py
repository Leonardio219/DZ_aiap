import random
import matplotlib.pyplot as plt
from io import BytesIO
import telebot
from telebot import types
STICKERS_ID = [
"CAACAgIAAxkBAAEOYAVoDmTzSXcXkr7JD3OQn2TuMd-QFgACAzUAAgzdEEsVnoF1pu4kTzYE",
"CAACAgIAAxkBAAEOYB9oDndO5U4f-ZFWcfAfrhWNX7o-GQACMTkAAilpEEtDmzik29ay3jYE",
'CAACAgIAAxkBAAEOYCFoDndknAfAVbHZ1niwP8_izF7a2AACpjsAAkf6YEvVJLX-YCeXljYE',
"CAACAgIAAxkBAAEOYCNoDneC9K293QioMqBe3dIPyxPGGgAC6kIAAlIkEUvyRcNUEetO-DYE",
"CAACAgIAAxkBAAEOYCVoDnnI_OIeMXHw6N6OzZgll9C4iAACUT0AArfpCUuQtqUY86FknzYE"
]
bot = telebot.TeleBot("7587179128:AAF9mOS7EDoCmfefNKRWhrCH5bMMwlwlXRI")
user_states = {}
user_data = {}
def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Стикер")
    button2 = types.KeyboardButton("График")
    keyboard.add(button1, button2)
    return keyboard
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, человек! Выберите действие:",
                                                reply_markup = create_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if text == "привет":
        bot.send_message(message.chat.id, "Привет, человек!")
    elif text == "стикер":
        send_sticker(message)
    elif text == "график":
        ask_for_k1(message)
    else:
        bot.send_message(message.chat.id, "Я не понимаю эту команду. Используйте кнопки.")
def send_sticker(message):
    if STICKERS_ID:
        sticker_id = random.choice(STICKERS_ID)
        bot.send_sticker(message.chat.id, sticker_id)
    else:
        bot.send_message(message.chat.id, "Стикеры не найдены.")
def ask_for_k1(message):
    msg = bot.send_message(message.chat.id, "Введите коэффициент k1 для уравнения"
                                                        "y = k1*x^2 + k2*x + k3:")
    bot.register_next_step_handler(msg, process_k1)
def process_k1(message):
    try:
        k1 = float(message.text)
        user_data[message.chat.id] = {'k1': k1}
        msg = bot.send_message(message.chat.id, "Теперь введите коэффициент k2:")
        bot.register_next_step_handler(msg, process_k2)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите число. Введите коэффициент k1:")
        bot.register_next_step_handler(msg, process_k1)
def process_k2(message):
    try:
        k2 = float(message.text)
        user_data[message.chat.id]['k2'] = k2
        msg = bot.send_message(message.chat.id, "Теперь введите коэффициент k3:")
        bot.register_next_step_handler(msg, process_k3)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите число. Введите коэффициент k2:")
        bot.register_next_step_handler(msg, process_k2)
def process_k3(message):
    try:
        k3 = float(message.text)
        user_data[message.chat.id]['k3'] = k3
        k1 = user_data[message.chat.id]['k1']
        k2 = user_data[message.chat.id]['k2']
        k3 = user_data[message.chat.id]['k3']
        x = range(0, 101)
        y = [k1 * xi ** 2 + k2 * xi + k3 for xi in x]
        plt.figure()
        plt.plot(x, y)
        plt.title(f"y = {k1}x² + {k2}x + {k3}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        bot.send_photo(message.chat.id, photo=buf)
        bot.send_message(message.chat.id, "График построен!", reply_markup=create_keyboard())
    except ValueError:
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите число. Введите коэффициент k3:")
        bot.register_next_step_handler(msg, process_k3)
if __name__ == '__main__':
    bot.polling(none_stop=True)