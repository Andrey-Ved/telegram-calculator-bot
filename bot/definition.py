import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from os.path import dirname, sep, abspath
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from sys import stdout

from bot.schemas import UsersCalc


logging.basicConfig(
    level=logging.INFO,
    stream=stdout,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',  # noqa
    datefmt='%H:%M:%S',
)


root_path = dirname(
    dirname(
        abspath(__file__)
    )
)

env_file = root_path + sep + '.env'


class Settings(BaseSettings):
    bot_token: SecretStr
    admin_username: SecretStr
    kb_prefix: str = 'num'
    kb_sep: str = '_'

    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding='utf-8',
    )


config = Settings()

users_calc: UsersCalc = {}

bot = Bot(
    token=config.bot_token.get_secret_value(),
    parse_mode=ParseMode.HTML
)

dp = Dispatcher(
    storage=MemoryStorage()
)
