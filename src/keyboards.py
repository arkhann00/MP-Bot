from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Карта МП 🗺️", callback_data="map")],
        [InlineKeyboardButton(text="Вступить в МП ⚡️",
                              url="https://forms.gle/DEYmN5mJfHeH6XpU8")],
    ], resize_keyboard=True)

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="main_menu")],
    ])