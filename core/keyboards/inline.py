from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

select_FAC = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="FAQ",
            callback_data="btn_fac_click"
        ),
        InlineKeyboardButton(
            text="Программа",
            callback_data="click_program"
        )
    ]
])

