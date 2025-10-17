from aiogram import Bot, Dispatcher
import asyncio

from src.settings import settings
from src.router import router as main_router

API_TOKEN = settings.BOT_TOKEN
print("Ура запустилось")
if not API_TOKEN or not API_TOKEN.strip():
    raise RuntimeError(f"BOT_TOKEN (или API_TOKEN) не задан. Проверь .env / compose \n Вот что в переменной {API_TOKEN}.")

bot = Bot(token=API_TOKEN)

dp = Dispatcher()

dp.include_router(main_router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())