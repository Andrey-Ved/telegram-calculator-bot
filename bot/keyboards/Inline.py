from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.definition import config


def get_keyboard(user_id: str) -> InlineKeyboardMarkup:
    prefix = config.kb_prefix + config.kb_sep + user_id + config.kb_sep
    buttons = [
        [
            InlineKeyboardButton(text="(", callback_data=prefix + "("),
            InlineKeyboardButton(text=")", callback_data=prefix + ")"),
            InlineKeyboardButton(text="AC", callback_data=prefix + "AC"),
            InlineKeyboardButton(text="C", callback_data=prefix + "C"),
        ],
        [
            InlineKeyboardButton(text="7", callback_data=prefix + "7"),
            InlineKeyboardButton(text="8", callback_data=prefix + "8"),
            InlineKeyboardButton(text="9", callback_data=prefix + "9"),
            InlineKeyboardButton(text="/", callback_data=prefix + "/"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data=prefix + "4"),
            InlineKeyboardButton(text="5", callback_data=prefix + "5"),
            InlineKeyboardButton(text="6", callback_data=prefix + "6"),
            InlineKeyboardButton(text="x", callback_data=prefix + "*"),
        ],
        [
            InlineKeyboardButton(text="1", callback_data=prefix + "1"),
            InlineKeyboardButton(text="2", callback_data=prefix + "2"),
            InlineKeyboardButton(text="3", callback_data=prefix + "3"),
            InlineKeyboardButton(text="-", callback_data=prefix + "-"),
        ],
        [
            InlineKeyboardButton(text="0", callback_data=prefix + "0"),
            InlineKeyboardButton(text="000", callback_data=prefix + "000"),
            InlineKeyboardButton(text=".", callback_data=prefix + "."),
            InlineKeyboardButton(text="+", callback_data=prefix + "+"),
        ],

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
