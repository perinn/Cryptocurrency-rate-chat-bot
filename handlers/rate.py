from aiogram import types
from bot_loader import dp
from states.getting_rate import GettingRate
from keyboards.crypto import crypto_menu
from keyboards.currency import currency_menu
from aiogram.dispatcher import FSMContext
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


@dp.message_handler(commands=["rate"], state=None)
async def bot_rate(message: types.Message):
    await message.answer(
        "Чтобы узнать курс криптовалюты к люобой из поддерживаемых валют, напишите ее название:",
        reply_markup=crypto_menu)

    await GettingRate.first()


@dp.message_handler(state=GettingRate.Q1)
async def answer_rate_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)

    await message.answer("Напишите название валюты:\nЧтобы узнать список поддерживаемых валют, напишите /supported_currency ", reply_markup=currency_menu)
    await GettingRate.next()


@dp.message_handler(state=GettingRate.Q2)
async def answer_rate_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    data = await state.get_data()
    answer1 = data.get("answer1")
    try:
        id1, name1 = cg.search(answer1)["coins"][0]['id'], cg.search(answer1)["coins"][0]['name']
        price = cg.get_price(ids=id1, vs_currencies=answer2)[id1][answer2]

        await message.answer(
            "На данный момент стоимость {name1} составляет:\n{price} {name2}".format(name1=name1, price=price,
                                                                                     name2=answer2),
            reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
    except:
        await message.answer(
            "Нет результатов",
            reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
