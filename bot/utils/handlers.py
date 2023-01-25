from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from bot.clients.api import api
from bot.utils.job import start_job


def start(update, _):
    update.message.reply_text('Welcome to lpdalle bot!', reply_markup=main_keyboard())


def get_user_generations(update, _) -> None:
    telegram_id = update.message.chat.id
    user = api.users.get_by_tg_id(telegram_id)
    generations = api.generation.get_for_user(user.uid)
    for gen in generations:
        update.message.reply_text(gen.prompt)


def add_generation(update, context):
    telegram_id = update.message.chat.id
    text = update.message.text
    update.message.reply_text('Добавляем генерацию')
    user = api.users.get_by_tg_id(telegram_id)

    if not user:
        login = update.message.chat.first_name.lower()
        api.users.add(
            login=login,
            email='awesomemail@foo.com',
            telegram_id=telegram_id,
        )
        user = api.users.get_by_tg_id(telegram_id)

    generation = api.generation.add(
        user_id=user.uid,
        prompt=text,
        status='pending',
    )

    context.job_queue.run_repeating(
        start_job,
        interval=5,
        first=5,
        context=[telegram_id, generation.uid],
    )

    return ConversationHandler.END


def main_keyboard():
    return ReplyKeyboardMarkup([['Генерировать картинку']], resize_keyboard=True)


def start_dialogue(update, _):
    update.message.reply_text('Введите текст для генерации', reply_markup=main_keyboard())
    return 'text'
