import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def start(update, context):
    update.message.reply_text('Welcome to lpdalle bot!')


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', start))

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()