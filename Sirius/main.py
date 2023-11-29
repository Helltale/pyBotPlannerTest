import config
import keyboard_menu
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token = config.BOT_TOKEN)
# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%H:%M - %d/%m/%Y")

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!") 


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")



# Хэндлер на команду /test2
@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Простой ответ")  


@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот непрерывно трудится для вас с   {started_at}")


if __name__ == "__main__":
    asyncio.run(main())
    
    
    