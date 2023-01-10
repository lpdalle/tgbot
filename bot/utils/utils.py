from bot.clients.api import api


def start(update, _):
    telegram_id = update.message.chat.id
    update.message.reply_text('Welcome to lpdalle bot!')
    api.users.get_by_tg_id(telegram_id)


def add_generation(update, _):
    telegram_id = update.message.chat.id
    update.message.reply_text('Add a generation')
    user = api.users.get_by_tg_id(telegram_id)
    if not user:
        api.users.add(
            login='topcoder',
            email='awesomemail@foo.com',
            telegram_id=telegram_id,
        )
    user_id = user['uid']
    api.generation.add(
        user_id=user_id,
        prompt='выхухоль в дирижабле',
        status='done',
    )
