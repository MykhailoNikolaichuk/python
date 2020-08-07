import os
import json
import logging
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

#some setup here
load_dotenv()
my_token = os.getenv('TOKEN')
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater.start_polling()


#functions here
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm stupid AF for now, maybe later on I'll will be able to read wow logs")

def echo(update, context):
    if 'salat' in update.message.text.lower():
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Salat is dumb fuck, that is everyone aware of')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'No, you are \'{update.message.text}\'')

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def fancy(update, context):
    text_fancy = ''.join([str(item).lower() if index % 2 == 0 else str(item).upper() for index, item in enumerate(list(' '.join(context.args)))])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_fancy)

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Idk what u mean. Are u Mr. Salateyshiy or what ?")


#binding and shipping here
start_handler       = CommandHandler('start', start)
echo_handler        = MessageHandler(Filters.text & (~Filters.command), echo)
caps_handler        = CommandHandler('caps', caps)
fancy_handler       = CommandHandler('fancy', fancy)
inline_caps_handler = InlineQueryHandler(inline_caps)
unknown_handler     = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(fancy_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)




# updater.stop()