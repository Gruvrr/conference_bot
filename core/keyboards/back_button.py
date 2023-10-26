from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="click_back"
        )
    ]
])

back_in_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="click_back_in_main_menu"
        )
    ]
])

back_on_message_13_dec = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="back_on_message_13_dec"
        )
    ]
])


back_on_sessions_time = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="back_on_time"
        )
    ]
])