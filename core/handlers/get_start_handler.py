from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import select_FAC


async def get_start(message: Message, bot: Bot ):
    await bot.send_message(message.from_user.id, (f"Здравствуйте, {message.from_user.first_name}.\n"
                                                 f"Благодарим за регистрацию на мероприятие!\n\n"
                                                  f"Ниже вы можете ознакомиться с программой мероприятия "
                                                  f"или посмотреть ответы на часто задаваемые вопросы."),
                                                    reply_markup=select_FAC)

