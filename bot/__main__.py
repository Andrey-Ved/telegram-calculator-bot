import asyncio

from aiogram.methods import DeleteWebhook
from platform import system

from bot.commands.commands import set_commands
from bot.commands.handlers import router as commands_router
from bot.definition import bot, dp
from bot.keyboards.callbacks import router as callbacks_router


async def main():
    dp.include_router(callbacks_router)
    dp.include_router(commands_router)

    await set_commands(bot)

    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)

    except (Exception, ):
        await bot.session.close()
        await dp.stop_polling()


if __name__ == '__main__':
    if system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
