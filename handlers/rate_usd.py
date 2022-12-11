from aiogram import types
from bot_loader import dp
from states.getting_rate_usd import GettingRateUsd
from keyboards.crypto import crypto_menu
from aiogram.dispatcher import FSMContext
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


@dp.message_handler(commands=["rate_usd"], state=None)
async def bot_rate_usd(message: types.Message):
    await message.answer("Чтобы узнать курс криптовалюты к usd, напишите ее название", reply_markup=crypto_menu)

    await GettingRateUsd.Q1.set()


@dp.message_handler(state=GettingRateUsd.Q1)
async def answer_rate_usd_q1(message: types.Message, state: FSMContext):
    answer = message.text
    try:
        id, name = cg.search(answer)["coins"][0]['id'], cg.search(answer)["coins"][0]['name']
        val = 'usd'
        price = cg.get_price(ids=id, vs_currencies=val)[id][val]

        await message.answer(
            "На данный момент стоимость {name} составляет:\n{price} {val}".format(name=name, price=price, val=val),
            reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    except:
        await message.answer(
            "Нет результатов",
            reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
