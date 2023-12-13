import telebot
from telebot import types
from datetime import datetime

TOKEN = '6623564412:AAGhSukh0xkUi0cZh0zdnV8nyww22y8JpW4'

bot = telebot.TeleBot(TOKEN)
db = {
    1: [
        'Algebra - 8:00-8:45',
        'Geometry - 8:55-9:40'
    ],
    6: [
        'Physics - 8:00-8:45',
        'English - 8:55- 9:40'
    ]
}
chat_id = ''
system_buttons = []


@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    print(f"{message.text} - {chat_id}")
    bot.send_message(chat_id, 'Welcome back, my friend!:', reply_markup=get_keyboard())


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_add_task = types.KeyboardButton(text="Add Task")
    button_get_tasks = types.KeyboardButton(text="Get Tasks")
    button_view_id = types.KeyboardButton(text="Start")
    keyboard.add(button_add_task, button_get_tasks, button_view_id)
    list_of_buttons = [button_add_task.text, button_get_tasks.text, button_view_id.text]
    system_buttons.extend(list_of_buttons) if not system_buttons else None
    return keyboard


def save(message):
    task = message.text.split()
    print(task)
    if chat_id not in db:
        db[chat_id] = {}

    print(system_buttons)
    if task[0] in system_buttons:
        return handle_messages(message)
    # db[chat_id].update({task[0]: [task[1] + datetime.now().strftime('%H:%M')]})
    bot.send_message(chat_id, 'Message saved', reply_markup=get_keyboard())


def get_messages(message):
    chat_id = message.chat.id
    day = datetime.today().weekday()
    result_task = '\n'.join(db[day])
    result = f"Today is: {datetime.now().strftime('%d/%m/%y - %A')}\n" \
             f"{result_task}"
    bot.send_message(chat_id, result)

    # if chat_id in db and db[chat_id]:
    #     print(db[chat_id])
    #     result = '\n'.join(db[chat_id], )
    #     bot.send_message(chat_id, result)
    # else:
    #     bot.send_message(chat_id, 'No records yet')


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # chat_id = message.chat.id

    if message.text == 'Add Task':
        bot.send_message(chat_id, 'Please, add task and datetime')
        bot.register_next_step_handler(message, save)
    elif message.text == 'Get Tasks':
        # bot.send_message(chat_id, 'GetTasks button pressed')
        get_messages(message)
    elif message.text == 'Start':
        message.text = '/start'
        start(message)
    else:
        bot.send_message(chat_id, message.text, reply_markup=get_keyboard())


if __name__ == '__main__':
    bot.polling()
