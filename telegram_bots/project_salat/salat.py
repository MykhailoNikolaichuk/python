import os
import json
import time
import logging
import draw_meme
from uuid import uuid4
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters



#some setup here
load_dotenv()
my_token = os.getenv('TOKEN')
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater.start_polling()
dispatcher.bot_data['top_text'] = 'САЛАТ'

#functions here
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='Hiya boi, wanna create some memes with Salat? \nTo create meme print:\n/top "your message"')

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Idk what u mean. Are u Mr. Salateyshiy or what ?")

def top(update, context):
    top_text = ' '.join(context.args).upper()
    context.bot_data['top_text'] = top_text
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text='Hehe, we almost done here print: \n/bot "your message"')

def bottom(update, context):
    bottom_text = ' '.join(context.args).upper()
    context.bot_data['bottom_text'] = bottom_text
    show(update, context)
    

def show(update, context):
    t_top_text = context.bot_data['top_text']
    t_bottom_text = context.bot_data['bottom_text']
    if t_top_text == '' and t_bottom_text == '':
        t_top_text = 'КЛАСНІ ТЕСТИ'
        t_bottom_text = 'ДАЙТЕ ЩЕ'
    u_id = time.time()
    draw_meme.get_salatifikado(
        t_top_text, 
        t_bottom_text, 
        f'./day18_meme/temp_meme_{u_id}.png')
    context.bot.send_photo(
        chat_id=update.effective_chat.id, 
        photo=open(f'./day18_meme/temp_meme_{u_id}.png', 'rb'))


#binding and shipping here
start_handler       = CommandHandler('start', start)
top_handler         = CommandHandler('top', top)
bottom_handler      = CommandHandler('bot', bottom)
unknown_handler     = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(top_handler)
dispatcher.add_handler(bottom_handler)
dispatcher.add_handler(unknown_handler)

# updater.stop()