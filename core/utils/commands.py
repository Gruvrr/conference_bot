from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Нажмите для старта бота'
        ),
        BotCommand(
            command='send_message1',
            description="Завтра мероприятие. Ждём вас!"
        ),
        BotCommand(
            command='send_message2',
            description="Отправить 13 декабря в 9 часов по МСК"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())