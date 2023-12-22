from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_commands(bot: Bot):
    data = [
        (
            [
                BotCommand(command="start_calc", description="New calculator"),
                BotCommand(command="close_calc", description="Close calculator"),
                BotCommand(command="stop_bot", description="Stop telegram bot")
            ],
            BotCommandScopeAllPrivateChats(),
            None
        )
    ]
    for commands_list, commands_scope, language in data:
        await bot.set_my_commands(
            commands=commands_list,
            scope=commands_scope,
            language_code=language,
        )
