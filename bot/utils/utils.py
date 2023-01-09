from bot.clients.api import api


def start(update, _):
    telegram_id = update.message.chat.id
    update.message.reply_text('Welcome to lpdalle bot!')
    api.users.get_by_tg_id(telegram_id)


def add_generation(update, _):
    telegram_id = update.message.chat.id
    update.message.reply_text('Add a generation')
    if not api.users.get_by_tg_id(telegram_id):
        api.users.add(
            login='topcoder',
            email='awesomemail@foo.com',
            telegram_id=telegram_id,
        )
    api.generation.add(
        # TODO: как брать user_id из telegram_id
        3,  # noqa: WPS432
        prompt='что-то в шляпе и очках',
        status='done',
    )
