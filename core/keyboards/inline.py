from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

select_FAC = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="FAC",
            callback_data="btn_fac_click"
        ),
        InlineKeyboardButton(
            text="Программа мероприятия",
            callback_data="click_program"
        )
    ]
])

