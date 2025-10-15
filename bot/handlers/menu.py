from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

# Кнопка 1 — информация об аккаунте
@router.message(F.text == "🧾 Моя подписка")
async def show_account_info(message: Message):
    # Здесь заглушка, но можно подключить базу данных позже
    text = (
        "🧾 <b>Информация об аккаунте</b>\n──────────\n"
        "👤 Пользователь: <b>@{}</b>\n"
        "⭐ Подписка: <b>Активна</b>\n"
        "📅 Действует до: <b>31.12.2025</b>\n"
        "💰 Баланс: <b>12.5 USDT</b>\n"
        "──────────\n"
        "Если хотите продлить подписку — обратитесь в поддержку 👇"
    ).format(message.from_user.username or "Без ника")

    await message.answer(text, parse_mode="HTML")

# Кнопка 2 — саппорт
@router.message(F.text == "💬 Поддержка")
async def contact_support(message: Message):
    text = (
        "💬 <b>Поддержка</b>\n──────────\n"
        "Если у вас возникли вопросы или проблемы — напишите нам:\n"
        "📩 <a href='https://t.me/support_username'>@support_username</a>\n\n"
        "Опишите проблему как можно подробнее, чтобы мы помогли быстрее 🧠"
    )
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)

@router.message(F.text == "Получить ключ")
async def get_key(massage: Message):
    text = (
        "Ваш ключ для доступа к VPN"
    )