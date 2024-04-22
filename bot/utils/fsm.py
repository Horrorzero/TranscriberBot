from aiogram.fsm.state import StatesGroup, State


#state for language
class Lang(StatesGroup):
    waiting_for_language = State()