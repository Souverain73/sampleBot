from telegram import Update


class BotState:
    stm = None

    def __init__(self, stm) -> None:
        self.stm = stm

    def handle_message(self, bot, update: Update):
        return

    def on_enter(self, bot, update: Update):
        return

    def on_exit(self, bot, update: Update):
        return

