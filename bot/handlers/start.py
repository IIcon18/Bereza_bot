from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.config.utils import load_users, save_users, generate_vless_link, create_subscription
from bot.keyboards.inline import main_menu

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message, command: CommandStart):
    users = load_users()
    user_id = str(message.from_user.id)
    username = message.from_user.username or "пользователь"
    tribute_token = command.args if command.args else None

    if user_id not in users:
        vless_link = generate_vless_link(user_id)
        subscription_end = create_subscription()

        users[user_id] = {
            "username": username,
            "vless_link": vless_link,
            "subscription_end": subscription_end,
            "tribute_token": tribute_token
        }
        save_users(users)

        text = (
            f"✅ Привет, @{username}!\n"
            f"Ваша подписка активирована 🔥\n\n"
            f"🔗 <b>VLESS-ссылка:</b>\n<code>{vless_link}</code>\n"
            f"📆 <b>Действует до:</b> {subscription_end}\n\n"
            f"▶️ Нажмите ниже, чтобы открыть видео-инструкцию."
        )
    else:
        vless_link = users[user_id]["vless_link"]
        subscription_end = users[user_id]["subscription_end"]
        text = (
            f"👋 Добро пожаловать обратно, @{username}!\n\n"
            f"🔗 <b>Ваша VLESS-ссылка:</b>\n<code>{vless_link}</code>\n"
            f"📆 <b>Подписка действует до:</b> {subscription_end}"
        )

    await message.answer(text, reply_markup=main_menu(), parse_mode="HTML")