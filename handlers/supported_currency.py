from aiogram import types

from bot_loader import dp
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


@dp.message_handler(commands=["supported_currency"])
async def get_supported_currency(message: types.Message):
    await message.answer("На данный момент поддерживаются следующие валюты:\n"+", ".join(cg.get_supported_vs_currencies()))
