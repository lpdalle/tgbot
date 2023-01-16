from telegram import ReplyKeyboardMarkup

from bot.clients.api import api


def start(update, context):
    update.message.reply_text('Welcome to lpdalle bot!', reply_markup=main_keyboard())


def add_generation(update, context):
    telegram_id = update.message.chat.id
    text = update.message.text
    update.message.reply_text('Добавляем генерацию')
    user = api.users.get_by_tg_id(telegram_id)
    login = update.message.chat.first_name.lower()

    if not user:
        api.users.add(
            login=login,
            email='awesomemail@foo.com',
            telegram_id=telegram_id,
        )
    user_id = user['uid']
    api.generation.add(
        user_id=user_id,
        prompt=text,
        status='pending',
    )


def main_keyboard():
    return ReplyKeyboardMarkup([['Генерировать картинку']], resize_keyboard=True)


def start_dialogue(update, context):
    update.message.reply_text('Введите текст для генерации', reply_markup=main_keyboard())
    return 'text'
