import logging

from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

from bot.clients.api import api
from bot.utils.handlers import add_generation, get_user_generations, start_dialogue
from bot.utils.menu import cmnd
from settings import API_KEY

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
)

logger = logging.getLogger(__name__)


def start(update, _) -> None:
    update.message.reply_text('Hi! Use /set <seconds> to set a timer')


def start_job(context) -> None:
    job = context.job
    chat_id = context.job.context[0]
    generation_id = context.job.context[1]
    generation = api.generation.check_status(generation_id)
    if generation.status != 'complete':
        context.bot.send_message(job.context[0], text='Task is not complete')
    else:
        image = api.generation.get_image(generation_id)
        context.bot.send_photo(chat_id, image)
        job.schedule_removal()


def start_queue(update, context) -> None:

    chat_id = update.message.chat_id
    generation_id = 19

    due = 5
    if due < 0:
        update.message.reply_text('Sorry we can not go back to future!')
        return

    context.job_queue.run_repeating(
        start_job,
        interval=due,
        first=3,
        context=[chat_id, generation_id],
    )


def main() -> None:
    my_bot = Updater(API_KEY, use_context=True)

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
    dp.add_handler(CommandHandler('set', start_queue))

    dp.add_handler(get_generation)

    logger.info('Bot has started')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
