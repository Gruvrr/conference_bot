from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Расписание сессий",
            callback_data="sessions"
        ),
        InlineKeyboardButton(
            text="Программа мероприятия",
            callback_data="click_program_13_dec"
        )
    ]
])