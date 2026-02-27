import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo

TOKEN = "ЧТОБЫ НЕ КРАЛИ МЫ УБРАЛИ))))))"
WEB_APP_URL = "https://tntbad.github.io/FinCity-Kids-MiniApp/FinCity-Kids-Site.html"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🚀 Открыть приложение", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])

    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Нажми на кнопку ниже, чтобы открыть приложение:",
        reply_markup=keyboard
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("Нажмите /start, чтобы начать!")

async def main():
    print("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Бот остановлен")
