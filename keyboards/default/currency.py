from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

currency_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="usd"),
            KeyboardButton(text="rub"),
            KeyboardButton(text="eur"),
            KeyboardButton(text="uah")
        ],
    ],
    resize_keyboard=True
)
