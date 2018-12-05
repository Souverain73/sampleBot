import collections
import logging

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

from statemachine.state_machine import StateMachine


def reply(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


handlers = {}


def handle_message(bot, update: Update):
    logging.info("В чате {}  получено сообщение с текстом [{}]".format(update.message.chat_id, update.message.text))
    chat_id = update.message.chat_id
    text = update.message.text

    if text == '/reset':
        handlers[chat_id] = None

    if handlers.get(chat_id) is None:
        handlers[chat_id] = StateMachine(bot, update)

    handlers[chat_id].handle_message(bot, update)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info("Bot is starting")

updater = Updater(token='799830075:AAGCbcEQ55ajnK4m1aohaa8BTkdJfaKsEVw')
start_handler = MessageHandler(Filters.text | Filters.command , handle_message)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)  # регистрируем в госреестре обработчиков

logging.info("Bot is configured")

updater.start_polling()
logging.info("READY")
