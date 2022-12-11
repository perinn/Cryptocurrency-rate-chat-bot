from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot_loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        "Привет, {}!\nЭто бот для быстрого поика курса криптовалюты\nЧтобы ознакомиться со списком команд, напиши\n/help".format(
            message.from_user.full_name))
