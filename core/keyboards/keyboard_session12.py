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
        InlineKeyboardButton(text="Зал 1", url='https://scienceplusbusiness.ru/9')
    ],
    [
        InlineKeyboardButton(text="Зал 2", url='https://scienceplusbusiness.ru/10')
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
        InlineKeyboardButton(text="Зал 3", url='https://scienceplusbusiness.ru/11')
    ],
    [
        InlineKeyboardButton(text="Зал 4", url='https://scienceplusbusiness.ru/12')
    ],
    [
        InlineKeyboardButton(text="Зал 5", url='https://scienceplusbusiness.ru/13')
    ],
    [
        InlineKeyboardButton(text="Зал 6", url='https://scienceplusbusiness.ru/14')
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
        InlineKeyboardButton(text="Зал 7", url='https://scienceplusbusiness.ru/15')
    ],
    [
        InlineKeyboardButton(text="Зал 8", url='https://scienceplusbusiness.ru/16')
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