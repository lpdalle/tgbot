from telegram import BotCommand

cmnd = []
cmnd.append(BotCommand('start', 'Start a bot'))
cmnd.append(BotCommand('mygenerations', 'See all my generations'))
cmnd.append(BotCommand('generate', 'Generate an image by string'))
