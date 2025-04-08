
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Main menu keyboard
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(
    KeyboardButton("1️⃣ Биолким маҳсулотлари 📦"),
    KeyboardButton("2️⃣ Экин турига қараб тавсиялар 🌱"),
)
menu_keyboard.add(
    KeyboardButton("3️⃣ Маслаҳат олиш 🧑‍💼"),
    KeyboardButton("4️⃣ Ўғит бериш календари 🗓️")
)
menu_keyboard.add(
    KeyboardButton("5️⃣ Савол-жавоб ❓"),
    KeyboardButton("6️⃣ Биз билан боғланиш 📞")
)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Ассалому алайкум! @Biolchimbot'га хуш келибсиз. Илтимос, керакли бўлимни танланг:",
        reply_markup=menu_keyboard,
    )

@dp.message_handler(lambda message: message.text)
async def handle_menu(message: types.Message):
    if message.text.startswith("1️⃣"):
        await message.answer("Биз сотувдаги барча маҳсулотлар тўғрисида маълумот берамиз.")
    elif message.text.startswith("2️⃣"):
        await message.answer("Қандай экин экилаётганига қараб тўғри ўғитларни танлашда ёрдам берамиз.")
    elif message.text.startswith("3️⃣"):
        await message.answer("Агрономимиздан саволларингизга жавоб олинг.")
    elif message.text.startswith("4️⃣"):
        await message.answer("Мавсум ва ўсиш босқичига қараб ўғит бериш жадвали.")
    elif message.text.startswith("5️⃣"):
        await message.answer("Кўп сўраладиган саволлар ва уларнинг жавоблари.")
    elif message.text.startswith("6️⃣"):
        await message.answer("Телефон рақамимиз ва ижтимоий тармоқлар орқали алоқа.")
    else:
        await message.answer("Илтимос, менюдан бирор бўлимни танланг.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
