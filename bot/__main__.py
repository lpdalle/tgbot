import logging

from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

from bot.utils.handlers import add_generation, start, start_dialogue
from bot.utils.menu import cmnd
from settings import API_KEY

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def main() -> None:
    my_bot = Updater(API_KEY, use_context=True)

    dp = my_bot.dispatcher

    my_bot.bot.set_my_commands(cmnd)

    get_generation = ConversationHandler(
        entry_points=[MessageHandler(
            Filters.regex('^(Генерировать картинку)|(generate)$'), start_dialogue,
        )],
        states={'text': [MessageHandler(Filters.text, add_generation)]},
        fallbacks=[],
    )

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(get_generation)

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
