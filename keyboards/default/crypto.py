from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crypto_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BTC"),
            KeyboardButton(text="ETH"),
            KeyboardButton(text="BNB"),
            KeyboardButton(text="XRP")
        ],
    ],
    resize_keyboard=True
)
