from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.saveMoney.constants import StoreKeys


class SaveMoneyState(BotState):
    def on_enter(self, bot, update: Update):
        bot.sendMessage(update.message.chat_id,
                        "Сохраняем {} рублей в категории [{}]. Комент: {}".format(self.stm.get_data(StoreKeys.VALUE),
                                                                                  self.stm.get_data(StoreKeys.CATEGORY),
                                                                                  self.stm.get_data(StoreKeys.COMMENT)))
        from statemachine.states.hello_state import HelloState
        self.stm.change_state(HelloState(self.stm), bot, update)