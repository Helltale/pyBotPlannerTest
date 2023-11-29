import keyboard_menu
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from datetime import datetime
from config_reader import config
from aiogram import F


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Объект бота
# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())


# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%H:%M - %d/%m/%Y")

# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(F: types.Message):
#     await F.answer("Hello!") 


# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(F: types.Message):
    await F.reply("Test 1")



# Хэндлер на команду /test2
@dp.message(Command("test2"))
async def cmd_test2(F: types.Message):
    await F.reply("Test 2")


@dp.message(Command("answer"))
async def cmd_answer(F: types.Message):
    await F.answer("Простой ответ")  


@dp.message(Command("бросить кубик"))
async def cmd_dice(F: types.Message):
    await F.answer_dice(emoji="🎲")


@dp.message(Command("info"))
async def cmd_info(F: types.Message, started_at: str):
    await F.answer(f"Бот непрерывно трудится для вас с   {started_at}")

@dp.message(Command("name"))
async def cmd_name(Message: types.Message):
    await Message.answer(f"Привет {Message.from_user.full_name}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Получить заметку"), types.KeyboardButton(text="Создать заметку")],
        [types.KeyboardButton(text="Просмотр заметок")],
        [types.KeyboardButton(text="Сколько я живу"), types.KeyboardButton(text="Кубик"), types.KeyboardButton(text="Пожаловаться")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите вариант ответа:"
    )
    await message.answer("start", reply_markup=keyboard)


@dp.message(F.text.lower() == "Кубик")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message(F.text.lower() == "Получить заметку")
async def selected_menu_main_1(message: types.Message):
    await message.reply("1")

@dp.message(F.text.lower() == "Создать заметку")
async def selected_menu_main_2(message: types.Message):
    await message.reply("2")

@dp.message(F.text.lower() == "Просмотр заметок")
async def selected_menu_main_3(message: types.Message):
    await message.reply("3")

if __name__ == "__main__":
    asyncio.run(main())
    