from aiogram import Router, types, F
from bot.config.utils import load_users
from bot.keyboards.inline import back_button, main_menu

router = Router()


@router.callback_query(F.data == "my_sub")
async def my_sub_callback(callback: types.CallbackQuery):
    users = load_users()
    user_id = str(callback.from_user.id)

    if user_id not in users:
        await callback.message.edit_text(
            "❌ Вы ещё не активировали подписку.",
            reply_markup=back_button()
        )
        return

    data = users[user_id]
    text = (
        f"📅 <b>Информация о подписке</b>\n\n"
        f"🔗 <b>VLESS:</b>\n<code>{data['vless_link']}</code>\n"
        f"📆 <b>Действует до:</b> {data['subscription_end']}"
    )
    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=back_button())


@router.callback_query(F.data == "back_main")
async def back_to_main(callback: types.CallbackQuery):
    username = callback.from_user.username or "пользователь"
    await callback.message.edit_text(
        f"👋 @{username}, выбери нужное действие ниже:",
        reply_markup=main_menu()
    )