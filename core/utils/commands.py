from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from core.settings import get_settings


async def set_commands(bot: Bot):
    admin_id = get_settings.bots.admin_id
    commands = [
        BotCommand(
            command='start',
            description='Нажмите для старта бота'
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())