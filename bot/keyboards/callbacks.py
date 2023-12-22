from aiogram import Router, F
from aiogram.types import CallbackQuery
from re import compile as re_compile

from bot.definition import users_calc, bot, config
from bot.keyboards.Inline import get_keyboard


router = Router()


async def calc(data: str) -> str:
    try:
        # with simple protection
        pattern = re_compile("[a-zA-Z]")

        if pattern.search(data) is None:
            return str(eval(data))

    except (Exception,):
        return ''


@router.callback_query(F.data.startswith(config.kb_prefix+config.kb_sep))
async def kb_callbacks(callback: CallbackQuery):
    user_id = callback.data.split(config.kb_sep)[1]

    if str(callback.from_user.id) != user_id:
        await bot.answer_callback_query(
            callback.id,
            "It's not your calculator"
        )
        return

    if (
            user_id not in users_calc
            or users_calc[user_id].message_id != callback.message.message_id
            or users_calc[user_id].chat_id != callback.message.chat.id
    ):
        await bot.answer_callback_query(
            callback.id,
            "Outdated calculator"
        )
        await bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
        )
        return

    action = callback.data.split("_")[2]

    if action == "AC":
        users_calc[user_id].row = ''
    elif action == "C":
        users_calc[user_id].row = users_calc[user_id].row[:-1]
    else:
        users_calc[user_id].row += action

    result = await calc(users_calc[user_id].row)

    await callback.message.edit_text(
        text=f'calculator for:   {users_calc[user_id].user_name}\n'
             f'{users_calc[user_id].row} \n'
             f'result:    {result}',
        reply_markup=get_keyboard(user_id)
    )

    await callback.answer()
