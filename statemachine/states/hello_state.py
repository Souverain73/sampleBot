from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.saveMoney.enter_category_state import EnterCategoryState


class HelloState(BotState):
    def handle_message(self, bot, update: Update):
        text = update.message.text
        if text == "/spent":
            self.stm.change_state(EnterCategoryState(self.stm), bot, update)
            return

        bot.sendMessage(update.message.chat_id, "Непонял, попробуй: /spent")

    def on_enter(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id, "Попробуй написать: /spent")
