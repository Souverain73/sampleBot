from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.saveMoney.constants import StoreKeys
from statemachine.states.saveMoney.enter_value_state import EnterValueState


class EnterCategoryState(BotState):
    def handle_message(self, bot, update: Update):
        category = update.message.text
        if category != '':
            self.stm.store_data(StoreKeys.CATEGORY, category)
            self.stm.change_state(EnterValueState(self.stm), bot, update)

    def on_enter(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id, "Введите категорию")

    def on_exit(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id, "Я это запомню")
