from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config.config import VIDEO_TUTORIAL_LINK, SUPPORT_USERNAME


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📅 Моя подписка", callback_data="my_sub")],
            [InlineKeyboardButton(text="▶️ Видео-инструкция", url=VIDEO_TUTORIAL_LINK)],
            [InlineKeyboardButton(text="🧑‍💬 Поддержка", url=f"https://t.me/{SUPPORT_USERNAME.strip('@')}")],
        ]
    )


def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")],
        ]
    )