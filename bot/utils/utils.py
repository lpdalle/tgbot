from bot.api_client import api


def start(update, _):
    update.message.reply_text('Welcome to lpdalle bot!')


def add_generation(update, context):
    update.message.reply_text('Add a generation')
    api.generation.add(17, prompt='розовый слон на дирижабле', status='done')  # noqa: WPS432
