from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from bot.config.config import VIDEO_TUTORIAL_LINK, SUPPORT_USERNAME


def main_menu():
    "Главная менюшк с подпиской и поддержкой"
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text= "🧾 Моя подписка")],
            [KeyboardButton(text= "💬 Поддержка")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def home_inline_keyboard():
    "Inline кнопка для видеоинструкции"
    Keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text= "Видеоинструкция", callback_data="VIDEO_TUTORIAL_LINK")]
        ]
    )
    return Keyboard

def back_button():
    "Кнопка назад"
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text= "↩︎ Назад")],
        ]
    )
    return keyboard