from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from src.keyboards import main_keyboard, back_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):

    await message.answer(text="Привет! Это бот МП!\nВозможности бота:\n- карта мп ( найти верующих в своем учебном заведении )\n- вступить в мп ( анкета )\n- ближайшие события ( перечени акций и мероприятий с регистрациями",
                         reply_markup=main_keyboard())

@router.callback_query(F.data == "map")
async def show_map(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Карта МП в разработке.", reply_markup=back_keyboard())
    await callback_query.answer("Карта МП будет доступна в ближайшее время.")
    # Здесь можно добавить логику для отображения карты, если она реализована

@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text="Привет! Это бот МП!\nВозможности бота:\n- карта мп ( найти верующих в своем учебном заведении )\n- вступить в мп ( анкета )\n- ближайшие события ( перечени акций и мероприятий с регистрациями",
                                           reply_markup=main_keyboard())

@router.callback_query(F.data == "events")
async def show_events(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Ближайшие события в разработке.", reply_markup=back_keyboard())
    await callback_query.answer("Ближайшие события будут опубликованы позже.")
    # Здесь можно добавить логику для отображения событий, если они реализованы
