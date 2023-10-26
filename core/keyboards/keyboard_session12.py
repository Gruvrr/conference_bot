from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


territory_keyboards12 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1. HR-территория", callback_data="hr12")
    ],
    [
        InlineKeyboardButton(text="2. Территория технологического предпринимательства", callback_data="technobis12")
    ],
    [
        InlineKeyboardButton(text="3. Территория науки, культуры и спорта", callback_data="since12")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="back_on_time")

    ]
])


keyboard_12hr = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 1", callback_data="hall1_12hr")
    ],
    [
        InlineKeyboardButton(text="Зал 2", callback_data="hall2_12hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="12")
    ]
])

back_12hr_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="hr12")
    ]
])


keyboard_12technobis = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 3", callback_data="hall3_12hr")
    ],
    [
        InlineKeyboardButton(text="Зал 4", callback_data="hall4_12hr")
    ],
    [
        InlineKeyboardButton(text="Зал 5", callback_data="hall5_12hr")
    ],
    [
        InlineKeyboardButton(text="Зал 6", callback_data="hall6_12hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="12")
    ]
])

back_12technobis_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="technobis10")
    ]
])




keyboard_12since = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Зал 7", callback_data="hall7_12hr")
    ],
    [
        InlineKeyboardButton(text="Зал 8", callback_data="hall8_12hr")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="12")
    ]
])

back_12since_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад",callback_data="since12")
    ]
])