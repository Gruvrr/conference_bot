from aiogram import Bot, Dispatcher
from core.handlers import get_start_handler
from core.settings import get_settings
from core.handlers import faq_handler,questions_handler, program_handler
import asyncio
import logging

async def start_bot(bot: Bot):
    await bot.send_message(get_settings.bots.admin_id, text="Bot is start")

async def stop_bot(bot: Bot):
    await bot.send_message(get_settings.bots.admin_id, text="Бот остановлен")

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] = %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=get_settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.message.register(get_start_handler.get_start)
    dp.callback_query.register(get_start_handler.get_start, lambda c: c.data == "click_back_in_main_menu")
    dp.callback_query.register(questions_handler.question_1, lambda c: c.data == "question_1")
    dp.callback_query.register(questions_handler.question_2, lambda c: c.data == "question_2")
    dp.callback_query.register(questions_handler.question_3, lambda c: c.data == "question_3")
    dp.callback_query.register(questions_handler.question_4, lambda c: c.data == "question_4")
    dp.callback_query.register(questions_handler.question_5, lambda c: c.data == "question_5")
    dp.callback_query.register(questions_handler.question_6, lambda c: c.data == "question_6")
    dp.callback_query.register(program_handler.view_program, lambda c: c.data == "click_program")
    dp.callback_query.register(faq_handler.btn_fac_click, lambda c: c.data == "btn_fac_click" or c.data == "click_back")

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())


