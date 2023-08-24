from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

def read_button(update, context):
    chat = update.effective_chat
    message = update.message.text
    if message == 'Посмотреть':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_message(
        chat_id=chat.id,
        text='Введите 1, если хотите посмотреть последнее сэлфи\nВведите 2, если хотите увидеть фото из старшей школы',
        reply_markup=button
        )
    elif message == '1':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_photo(chat.id, open('image/1.jpg', 'rb'), reply_markup=button)
    elif message == '2':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_photo(chat.id, open('image/2.jpg', 'rb'), reply_markup=button)
    elif message == 'Почитать пост про увлечения':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_message(
        chat_id=chat.id,
        text='Я люблю проводить свободное время за увлекательными занятиями. '
            'Одним из моих любимых увлечений является раскрашивание картин по номерам и сбор алмазных мозаик. '
            'Эти занятия помогают мне расслабиться, отвлечься от повседневных забот. '
            'Я также люблю читать книги(в последнее время это книги о работе мозга) и смотреть фильмы и, конечно, сериальчики.',
        reply_markup=button
        )
    elif message == 'Прислать войс':
        button = ReplyKeyboardMarkup([['Что такое GPT?'], ['Разница между SQL и NoSQL'], ['История первой любви'], ['Назад']], resize_keyboard=True)
        context.bot.send_message(
        chat_id=chat.id,
        text='Что ты хочешь послушать?',
        reply_markup=button
        )
    elif message == 'Что такое GPT?':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_voice(
            chat_id=chat.id,
            voice = open('voice/GPT.ogg', 'rb'),
            reply_markup=button
        )
    elif message == 'Разница между SQL и NoSQL':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_voice(
            chat_id=chat.id,
            voice = open('voice/SQL.ogg', 'rb'),
            reply_markup=button
        )
    elif message == 'История первой любви':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_voice(
            chat_id=chat.id,
            voice = open('voice/love.ogg', 'rb'),
            reply_markup=button
        )
    elif message == 'Назад':
        button = ReplyKeyboardMarkup([['Посмотреть'], ['Почитать пост про увлечения'], ['Прислать войс'], ['Получить ссылку на репозиторий']])
        context.bot.send_message(
        chat_id=chat.id,
        text='Куда отправимся теперь?',
        reply_markup=button  
        )
    elif message == 'Получить ссылку на репозиторий':
        button = ReplyKeyboardMarkup([['Назад']], resize_keyboard=True)
        context.bot.send_message(
        chat_id=chat.id,
        text='https://github.com/mnk96/practikum_kids_ai',
        reply_markup=button  
        )
    else:
        context.bot.send_message(
        chat_id=chat.id,
        text='Такой команды нет, попробуй ещё раз'
        )
    
def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['Посмотреть фотографии'], ['Почитать пост про увлечения'], ['Прислать войс'], ['Получить ссылку на репозиторий']])
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}!'.format(name),
        reply_markup=button  
        )

def main():
    updater = Updater(token=TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, read_button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()