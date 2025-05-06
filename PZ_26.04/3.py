import telebot
from telebot import types

BOT_TOKEN = '7587179128:AAF9mOS7EDoCmfefNKRWhrCH5bMMwlwlXRI'

bot = telebot.TeleBot(BOT_TOKEN)

tasks = {}

# команда старт и добавление строк
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Добавить задачу")
    button2 = types.KeyboardButton("Посмотреть список задач")
    button3 = types.KeyboardButton("Удалить задачу")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, "Привет! Я бот для управления вашими задачами. Выберите команду:", reply_markup=markup)

# Обработка нажатий кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Добавить задачу":
        add_task(message)
    elif message.text == "Посмотреть список задач":
        show_tasks(message)
    elif message.text == "Удалить задачу":
        delete_task(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите одну из доступных команд.")

# Команда добавить задачу
def add_task(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите текст задачи:")
    bot.register_next_step_handler(message, process_task_text)

def process_task_text(message):
    chat_id = message.chat.id
    task_text = message.text

    # Получаем список задач пользователя или создаем новый
    if chat_id in tasks:
        user_tasks = tasks[chat_id]
    else:
        user_tasks = []
        tasks[chat_id] = user_tasks

    # Добавляем задачу в список
    user_tasks.append(task_text)
    bot.send_message(chat_id, f"Задача '{task_text}' добавлена в ваш список.")

# Обработчик команды /showtasks
def show_tasks(message):
    chat_id = message.chat.id

    # Получаем список задач пользователя
    if chat_id in tasks:
        user_tasks = tasks[chat_id]
    else:
        user_tasks = []

    # Проверяем, есть ли задачи
    if not user_tasks:
        bot.send_message(chat_id, "Ваш список задач пуст.")
        return

    # Формируем сообщение со списком задач
    task_list_text = "Ваш список задач:\n"
    for i, task in enumerate(user_tasks):
        task_list_text += f"{i + 1}. {task}\n"

    bot.send_message(chat_id, task_list_text)

# Обработчик команды /deltask
def delete_task(message):
    chat_id = message.chat.id

    # Получаем список задач пользователя
    if chat_id in tasks:
        user_tasks = tasks[chat_id]
    else:
        user_tasks = []

    # Проверяем, есть ли задачи
    if not user_tasks:
        bot.send_message(chat_id, "Ваш список задач пуст. Нечего удалять.")
        return

    # Формируем сообщение со списком задач для выбора
    task_list_text = "Ваш список задач:\n"
    for i, task in enumerate(user_tasks):
        task_list_text += f"{i + 1}. {task}\n"

    bot.send_message(chat_id, task_list_text + "\nВведите номер задачи для удаления:")
    bot.register_next_step_handler(message, process_delete_number)

def process_delete_number(message):
    chat_id = message.chat.id
    try:
        task_number = int(message.text)
    except ValueError:
        bot.send_message(chat_id, "Пожалуйста, введите целое число - номер задачи.")
        return

    # Получаем список задач пользователя
    user_tasks = tasks[chat_id]

    # Проверяем корректность номера задачи
    if 1 <= task_number <= len(user_tasks):
        deleted_task = user_tasks.pop(task_number - 1)
        bot.send_message(chat_id, f"Задача '{deleted_task}' удалена.")
        # Обновляем список задач пользователя в словаре
        tasks[chat_id] = user_tasks
    else:
        bot.send_message(chat_id, "Неверный номер задачи. Пожалуйста, введите номер из списка.")

# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()