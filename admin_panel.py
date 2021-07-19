from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data import config
from keyboards.default.admin_panel import admin_panel_keyboard, admin_panel_keyboard_category
from loader import dp
from states.admin_panel_state import AdminAppend


@dp.message_handler(Command('Admin'), user_id=config.admins)
async def admin_panel(message: types.Message):
    await message.answer('🛠Панель администратора🛠\n'
                         'Выберите категорию где нужно сделать измениния', reply_markup=admin_panel_keyboard_category)


@dp.message_handler(text='Instagram', user_id=config.admins)
async def admin_panel_append(message: types.Message):
    await message.answer('Выберите категорию', reply_markup=admin_panel_keyboard)


@dp.message_handler(text='Добавить товар', user_id=config.admins)
async def admin_panel_instagram(message: types.Message, state: FSMContext):
    await message.answer('Введите названия товара')
    await AdminAppend.one.set()


@dp.message_handler(user_id=config.admins, state=AdminAppend.one)
async def description(message: types.Message, state: FSMContext):
    title = message.text
    await message.answer('Введите описания товара')
    await AdminAppend.next()



