from telegram import Update, Bot

from statemachine.states.bot_state import BotState
from statemachine.states.hello_state import HelloState


class InitialState(BotState):
    def handle_message(self, bot, update: Update):
        if update.message.text == '/start':
            self.stm.change_state(HelloState(self.stm), bot, update)

    def on_enter(self, bot: Bot, update: Update):
        bot.send_message(update.message.chat_id, "write /start to start")
