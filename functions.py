from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Click", callback_data="get_id")

    await message.answer(
        "Salom 👍",
        reply_markup=kb.as_markup()
    )

@router.callback_query(F.data == "get_id")
async def get_id(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    user_id = callback.from_user.id

    await callback.message.answer(
        f"Chat id: {chat_id}\nUser_id: {user_id}"
    )
    await callback.answer()
