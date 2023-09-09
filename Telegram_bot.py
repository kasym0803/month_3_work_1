

import asyncio
from dotenv import load_dotenv
from os import getenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    # await message.reply("Привет")
    await message.answer("Привет")


@dp.message(Command("photo"))
async def send_photo(message: types.Message):
    file = types.FSInputFile("photo_car.jpg")
    await message.answer_photo(file)


@dp.message(Command("info"))
async def info(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        f"Привет {message.from_user.first_name}\nid: {message.from_user.id}",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())