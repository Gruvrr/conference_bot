from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

keyboard_time = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="10:00 - 11:45",
            callback_data="10"
        ),
        InlineKeyboardButton(
            text="12:00 - 13:30",
            callback_data="12"
        ),
        InlineKeyboardButton(
            text="14:00 - 16:00",
            callback_data="14"
        )
    ]
])


territory_keyboards10 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1. HR-территория", callback_data="hr10")
    ],
    [
        InlineKeyboardButton(text="2. Территория технологического предпринимательства", callback_data="technobis10")
    ],
    [
        InlineKeyboardButton(text="3. Территория науки, культуры и спорта", callback_data="since10")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_on_time")

    ]
])


keyboard_10hr = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 1", callback_data="hall1_10hr")
    ],
    [
        InlineKeyboardButton(text="Зал 2", callback_data="hall2_10hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="10")
    ]
])

back_10hr_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="hr10")
    ]
])


keyboard_10technobis = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 3", callback_data="hall3_10hr")
    ],
    [
        InlineKeyboardButton(text="Зал 4", callback_data="hall4_10hr")
    ],
    [
        InlineKeyboardButton(text="Зал 5", callback_data="hall5_10hr")
    ],
    [
        InlineKeyboardButton(text="Зал 6", callback_data="hall6_10hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="10")
    ]
])

back_10technobis_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="technobis10")
    ]
])




keyboard_10since = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 7", callback_data="hall7_10hr")
    ],
    [
        InlineKeyboardButton(text="Зал 8", callback_data="hall8_10hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="10")
    ]
])

back_10since_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="since10")
    ]
])