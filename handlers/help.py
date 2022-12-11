from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot_loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/rate_usd - Узнать курс криптовалюты к usd",
            "/rate - Узнать курс криптовалюты",
            "/supported_currency - Узнать поддрежвиаемые валюты")
    
    await message.answer("\n".join(text))
