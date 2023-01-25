from bot.clients.api import api


def start_job(context) -> None:
    job = context.job
    chat_id = context.job.context[0]
    generation_id = context.job.context[1]
    generation = api.generation.check_status(generation_id)

    if generation.status != 'complete':
        context.bot.send_message(job.context[0], text='картинка генерируется')
        return

    image = api.generation.get_image(generation_id)
    context.bot.send_photo(chat_id, image)
    job.schedule_removal()
