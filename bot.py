import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "1773149086:AAHNVvFpfC4Yk0eIJFns8jRID-ToWo84HvQ"
# bot name is @nlp_to_sql_bot

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

F_MESSAGE = "Приветствую, введите предложение и бот ответит sql запросом"


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=F_MESSAGE)


def translate(update, context):
    nlp_request = update.message.text
    #do something with nlp
    sql_request = nlp_request
    context.bot.send_message(chat_id=update.effective_chat.id, text=sql_request)


start_handler = CommandHandler('start', start)
translate_handler = MessageHandler(Filters.text & (~Filters.command), translate)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(translate_handler)

updater.start_polling()
updater.idle()