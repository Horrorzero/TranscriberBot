from aiogram.fsm.state import StatesGroup, State


#state for language
class SttLang(StatesGroup):
    waiting_for_language = State()