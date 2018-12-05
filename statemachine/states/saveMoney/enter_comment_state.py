from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.saveMoney.constants import StoreKeys
from statemachine.states.saveMoney.save_money_state import SaveMoneyState


class EnterCommentState(BotState):
    def handle_message(self, bot, update: Update):
        comment = update.message.text
        if comment == '':
            return

        if comment != '/skip':
            self.go_next(bot, update)
            return

        self.stm.store_data(StoreKeys.COMMENT, comment)
        self.go_next(bot, update)

    def on_enter(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id, "Введите коментарий или '/skip' если нечего прокоментировать")

    def go_next(self, bot, update):
        self.stm.change_state(SaveMoneyState(self.stm), bot, update)
