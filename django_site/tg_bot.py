import telebot
from telebot import types
from datetime import datetime

TOKEN = '6623564412:AAGhSukh0xkUi0cZh0zdnV8nyww22y8JpW4'

bot = telebot.TeleBot(TOKEN)
db = {
    0: [
        'Physics - 8:00-8:45',
        'English - 8:55-9:40',
    ],
    6: [
        'Algebra - 8:00-8:45',
        'Geometry - 8:55-9:40',
    ]
}

days_of_week = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

chat_id = ''
system_buttons = []


@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    print(f"{message.text} - {message.from_user.first_name}")

    bot.send_message(chat_id, f"Welcome back, {message.from_user.first_name}", reply_markup=get_keyboard())


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_choice_day = types.KeyboardButton(text="Choose day")
    button_get_tasks = types.KeyboardButton(text="Today Tasks")
    button_start = types.KeyboardButton(text="Start")
    keyboard.add(button_choice_day, button_get_tasks, button_start)
    list_of_buttons = [button_choice_day.text, button_get_tasks.text, button_start.text]
    system_buttons.extend(list_of_buttons) if not system_buttons else None
    return keyboard


def get_days_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    monday = types.KeyboardButton(text="Monday")
    tuesday = types.KeyboardButton(text="Tuesday")
    wednesday = types.KeyboardButton(text="Wednesday")
    thursday = types.KeyboardButton(text="Thursday")
    friday = types.KeyboardButton(text="Friday")

    keyboard.add(monday, tuesday, wednesday, thursday, friday)
    back_button = types.KeyboardButton(text="Back to start")
    keyboard.add(back_button)
    return keyboard


def save(message):
    task = message.text.split()
    # print(task)
    # if chat_id not in db:
    #     db[chat_id] = {}

    print(system_buttons)
    if task[0] in system_buttons:
        return handle_messages(message)
    # db[chat_id].update({task[0]: [task[1] + datetime.now().strftime('%H:%M')]})
    bot.send_message(chat_id, 'Message saved', reply_markup=get_keyboard())


def get_messages(message):
    chat_id = message.chat.id
    day = datetime.today().weekday()
    print(day)

    if day in db:
        result_day = f"Today is: {datetime.now().strftime('%A, %d/%m/%y')}\n"
        result_day += '\n'.join(db[day])
        bot.send_message(chat_id, result_day)
    else:
        bot.send_message(chat_id, 'No records yet')


def get_messages_for_day(message):
    
    if message.text == 'Back to start':
        return start(message)

    day = days_of_week[message.text]
    result_for_day = f"Schedule for {message.text}:\n"
    result_for_day += '\n'.join(db[day])
    bot.send_message(chat_id, result_for_day, reply_markup=get_days_keyboard())


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # chat_id = message.chat.id

    if message.text == 'Choose day':
        bot.send_message(chat_id, 'Choose day to view schedule', reply_markup=get_days_keyboard())
        bot.register_next_step_handler(message, get_messages_for_day)
    elif message.text == 'Today Tasks':
        # bot.send_message(chat_id, 'GetTasks button pressed')
        get_messages(message)
    elif message.text == 'Start':
        start(message)
    else:
        bot.send_message(chat_id, 'Please choose element in bottom menu ', reply_markup=get_keyboard())


if __name__ == '__main__':
    bot.infinity_polling()
