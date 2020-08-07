import json

from dotenv import load_dotenv
load_dotenv()

import os
my_token = os.getenv('TOKEN')
# print(token)

# import telegram
# bot = telegram.Bot(token=token)
# print(bot.get_me())

from telegram.ext import Updater
updater = Updater(token=my_token, use_context=True)


dispatcher = updater.dispatcher


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm stupid AF for now, maybe later on I'll will be able to read wow logs")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()


def echo(update, context):
    if update.message.text.lower() == 'salat':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Salat is dumb fuck, that is everyone aware of')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'No, you are \'{update.message.text}\'')

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def fancy(update, context):
    text_fancy = ''.join([str(item).lower() if index % 2 == 0 else str(item).upper() for index, item in enumerate(list(' '.join(context.args)))])
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_fancy)

fancy_handler = CommandHandler('fancy', fancy)
dispatcher.add_handler(fancy_handler)


from telegram import InlineQueryResultArticle, InputTextMessageContent
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

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)



def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Idk what u mean. Are u Mr. Salateyshiy or what ?")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



# updater.stop()