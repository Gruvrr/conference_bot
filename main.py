from aiogram import Bot, Dispatcher
from core.handlers import get_start_handler
from core.settings import get_settings
from core.handlers import (faq_handler,
                           questions_handler,
                           program_handler,
                           tomorrow_handler,
                           conference_today_handler,
                           sessions_handler)

import asyncio
import logging
from core.utils.commands import set_commands
from aiogram.filters import Command


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(get_settings.bots.admin_id, text="Bot is start")


async def stop_bot(bot: Bot):
    await bot.send_message(get_settings.bots.admin_id, text="Бот остановлен")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] = %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=get_settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.message.register(get_start_handler.get_start, Command("start"))
    dp.message.register(tomorrow_handler.send_conference_tomorrow, Command("send_message1"))
    dp.message.register(conference_today_handler.send_today_conference_message, Command("send_message2"))
    dp.callback_query.register(get_start_handler.get_start, lambda c: c.data == "click_back_in_main_menu")
    dp.callback_query.register(questions_handler.question_1, lambda c: c.data == "question_1")
    dp.callback_query.register(questions_handler.question_2, lambda c: c.data == "question_2")
    dp.callback_query.register(questions_handler.question_3, lambda c: c.data == "question_3")
    dp.callback_query.register(questions_handler.question_4, lambda c: c.data == "question_4")
    dp.callback_query.register(questions_handler.question_5, lambda c: c.data == "question_5")
    dp.callback_query.register(questions_handler.question_6, lambda c: c.data == "question_6")
    dp.callback_query.register(program_handler.view_program, lambda c: c.data == "click_program")
    dp.callback_query.register(sessions_handler.choice_time_10, lambda c: c.data == "10")
    dp.callback_query.register(sessions_handler.choice_time_12, lambda c: c.data == "12")
    dp.callback_query.register(sessions_handler.choice_time_15, lambda c: c.data == "15")
    dp.callback_query.register(program_handler.view_program_13_dec, lambda c: c.data == "click_program_13_dec")
    dp.callback_query.register(sessions_handler.choice_session, lambda c: c.data == "sessions" or c.data == "back_on_session_timegit rm --cached .gitignore")
    dp.callback_query.register(conference_today_handler.send_today_conference_callback,
                               lambda c: c.data == "back_on_message_13_dec")


    dp.callback_query.register(faq_handler.btn_fac_click, lambda c: c.data == "btn_fac_click" or c.data == "click_back")

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())


