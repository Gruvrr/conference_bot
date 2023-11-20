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
        InlineKeyboardButton(text="Зал 1", url='https://scienceplusbusiness.ru/1')
    ],
    [
        InlineKeyboardButton(text="Зал 2", url='https://scienceplusbusiness.ru/2')
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
        InlineKeyboardButton(text="Зал 3", url='https://scienceplusbusiness.ru/3')
    ],
    [
        InlineKeyboardButton(text="Зал 4", url='https://scienceplusbusiness.ru/4')
    ],
    [
        InlineKeyboardButton(text="Зал 5", url='https://scienceplusbusiness.ru/5')
    ],
    [
        InlineKeyboardButton(text="Зал 6", url='https://scienceplusbusiness.ru/6')
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
        InlineKeyboardButton(text="Зал 7", url='https://scienceplusbusiness.ru/7')
    ],
    [
        InlineKeyboardButton(text="Зал 8", url='https://scienceplusbusiness.ru/8')
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