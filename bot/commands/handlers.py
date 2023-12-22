from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.definition import config, bot, dp, users_calc
from bot.keyboards.Inline import get_keyboard
from bot.schemas import UserCalc, UserID


router = Router()


async def closing_old_calculator(user_id: UserID):
    if user_id in users_calc:
        await bot.delete_message(
            chat_id=users_calc[user_id].chat_id,
            message_id=users_calc[user_id].message_id,
        )
        del users_calc[user_id]


@router.message(Command("start_calc"))
async def start_calc(message: Message):
    user_id = str(message.from_user.id)

    await closing_old_calculator(user_id)

    answer_message = await message.answer(
        text=f'calculator for:   {message.from_user.username}\n'
             f' \n'
             f'result:    0',
        reply_markup=get_keyboard(user_id)
    )

    users_calc[user_id] = UserCalc(
        user_name=message.from_user.username,
        row='',
        message_id=answer_message.message_id,
        chat_id=answer_message.chat.id
    )

    await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id,
    )


@router.message(Command("close_calc"))
async def close_calc(message: Message):
    user_id = str(message.from_user.id)

    await closing_old_calculator(user_id)

    await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id,
    )


@router.message(Command("stop_bot"))
async def stop_bot(message: Message):
    user_name = message.from_user.username

    if user_name != config.admin_username.get_secret_value():
        return

    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id,
    )

    running_calc = list(users_calc.keys())

    for user_id in running_calc:
        await closing_old_calculator(user_id)

    await dp.stop_polling()
    await bot.session.close()
