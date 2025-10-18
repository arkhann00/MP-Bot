from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


def main_keyboard():
    map_mini_app = "https://map.moepokolenie.ru/"
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Карта МП 🗺️", web_app=WebAppInfo(url=map_mini_app))],
        [InlineKeyboardButton(text="Вступить в МП ⚡️",
                              url="https://forms.gle/DEYmN5mJfHeH6XpU8")],
    ], resize_keyboard=True)

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="main_menu")],
    ])