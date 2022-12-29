import logging

from telegram.ext import CommandHandler, Updater

import settings
from bot.utils.utils import add_generation, start

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('generate', add_generation))

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
