from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Карта МП 🗺️", callback_data="map"),
         InlineKeyboardButton(text="Ближайшие события 🔥", callback_data="events")],
        [InlineKeyboardButton(text="Вступить в МП ⚡️",
                              url="https://docs.google.com/forms/d/e/1FAIpQLSdlqzArM0zpNGjoPxheXcLzu0pScaU56315Qtx0JLdgUXie0g/viewform")],
    ], resize_keyboard=True)

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="main_menu")],
    ])