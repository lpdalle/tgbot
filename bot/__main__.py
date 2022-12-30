import logging

from telegram import BotCommand
from telegram.ext import CommandHandler, Updater

from bot.utils.utils import add_generation, start
from settings import API_KEY

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():
    my_bot = Updater(API_KEY, use_context=True)

    dp = my_bot.dispatcher
    cmnd = []
    cmnd.append(BotCommand('start', 'Start a bot'))
    cmnd.append(BotCommand('mygenerations', 'See all my generations'))
    cmnd.append(BotCommand('generate', 'Generate an image by string'))
    my_bot.bot.set_my_commands(cmnd)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('generate', add_generation))

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
