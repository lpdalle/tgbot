import logging

from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

from bot.config import conf
from bot.utils.handlers import add_generation, get_user_generations, start, start_dialogue
from bot.utils.menu import cmnd

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main() -> None:
    my_bot = Updater(conf.api_key, use_context=True)

    dp = my_bot.dispatcher  # type: ignore

    my_bot.bot.set_my_commands(cmnd)  # type: ignore

    get_generation = ConversationHandler(
        entry_points=[MessageHandler(
            Filters.regex('^(Генерировать картинку)|(generate)$'), start_dialogue,
        )],
        states={'text': [MessageHandler(Filters.text, add_generation)]},
        fallbacks=[],
    )

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('mygenerations', get_user_generations))

    dp.add_handler(get_generation)

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
