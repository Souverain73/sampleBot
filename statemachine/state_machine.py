import logging

from telegram import Update

from statemachine.states.bot_state import BotState
from statemachine.states.initial_state import InitialState


class StateMachine:
    state: BotState = None
    store = {}

    def __init__(self, bot, update) -> None:
        self.change_state(InitialState(self), bot, update)
        logging.info("Crete state machine for chat {}".format(update.message.chat_id))

    def change_state(self, state: BotState, bot, update):
        logging.info("Change state for chat {}".format(update.message.chat_id))

        if self.state is not None:
            self.state.on_exit(bot, update)

        self.state = state
        self.state.on_enter(bot, update)

    def handle_message(self, bot, update: Update):
        logging.info("Handle message in chat {}".format(update.message.chat_id))
        self.state.handle_message(bot, update)

    def store_data(self, key, value):
        self.store[key] = value

    def get_data(self, key):
        return self.store.get(key)