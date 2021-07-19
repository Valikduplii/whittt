from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminAppend(StatesGroup):
    one = State()
    two = State()
    three = State()


class AdminPop(StatesGroup):
    one = State()
    two = State()
    three = State()


class AdminInsert(StatesGroup):
    one = State()
    two = State()
    three = State()