from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.saveMoney.constants import StoreKeys
from statemachine.states.saveMoney.enter_comment_state import EnterCommentState


class EnterValueState(BotState):
    value = 0

    def __init__(self, stm, ) -> None:
        super().__init__(stm)

    def handle_message(self, bot, update: Update):
        value = update.message.text
        try:
            int_value = int(value)
        except Exception:
            bot.sendMessage(update.message.chat_id, "Введите корректную сумму:")
            return

        self.stm.store_data(StoreKeys.VALUE, int_value)
        self.value = int_value
        self.stm.change_state(EnterCommentState(self.stm), bot, update)

    def on_enter(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id, "Введите сумму:")

    def on_exit(self, bot, update: Update):
        if self.value > 500:
            bot.sendMessage(update.message.chat_id, "Это уже похоже на деньги, продолжим")
