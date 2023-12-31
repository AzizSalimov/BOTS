import telebot
from environs import Env

env = Env()
env.read_env()
BOT_TOKEN = '6385019069:AAFxRYzQLaJ5kU-dFvFagAIHKkfMndaY7qk'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id,
                     f"Hello {user.first_name} \n"
                     f"The task of this bot is to find your age")


@bot.message_handler(func=lambda message: int)
def meesage_age(message):
    ms = message.text
    bot.reply_to(message, f"Ваш возраст равна --> {2023 - int(ms)} годам.")


if __name__ == "__main__":
    bot.infinity_polling()
