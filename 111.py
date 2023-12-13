import telebot
from telebot import types

# Your Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Dictionary to store tasks by user ID
tasks = {}

# Function to create a keyboard with multiple buttons
def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_add_task = types.KeyboardButton(text="Add Task")
    button_get_tasks = types.KeyboardButton(text="Get Tasks")
    keyboard.add(button_add_task, button_get_tasks)
    return keyboard

# Handler to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome! Please select an option:", reply_markup=get_keyboard())

# Handler for button clicks
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id

    if message.text == 'Add Task':
        bot.send_message(chat_id, "Enter your task:")
        bot.register_next_step_handler(message, save_task)
    elif message.text == 'Get Tasks':
        get_tasks(message)

# Function to save the task
def save_task(message):
    chat_id = message.chat.id
    user_task = message.text

    if chat_id not in tasks:
        tasks[chat_id] = []

    tasks[chat_id].append(user_task)
    bot.send_message(chat_id, "Task added successfully! Please select an option:", reply_markup=get_keyboard())

# Function to get tasks
def get_tasks(message):
    chat_id = message.chat.id

    if chat_id in tasks and tasks[chat_id]:
        tasks_text = "\n".join(tasks[chat_id])
        bot.send_message(chat_id, f"Your tasks:\n{tasks_text}")
    else:
        bot.send_message(chat_id, "You have no tasks yet.")

# Start the bot
bot.polling()
