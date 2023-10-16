from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

keyboard_time = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="10:00 - 11:45",
            callback_data="10"
        ),
        InlineKeyboardButton(
            text="12:15 - 14:00",
            callback_data="12"
        ),
        InlineKeyboardButton(
            text="15:00 - 17:00",
            callback_data="15"
        )
    ]
])

keyboard_10 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Зал 1",
            callback_data="Hall_1_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 2",
            callback_data="Hall_2_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 3",
            callback_data="Hall_3_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 4",
            callback_data="Hall_4_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 5",
            callback_data="Hall_5_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 6",
            callback_data="Hall_6_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 7",
            callback_data="Hall_7_10"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 8",
            callback_data="Hall_8_10"
        )
    ],[
        InlineKeyboardButton(
            text="Back",
            callback_data="back_on_sessions_time"
        )
    ]
])


keyboard_12 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Зал 1",
            callback_data="Hall_1_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 2",
            callback_data="Hall_2_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 3",
            callback_data="Hall_3_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 4",
            callback_data="Hall_4_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 5",
            callback_data="Hall_5_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 6",
            callback_data="Hall_6_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 7",
            callback_data="Hall_7_12"
        )
    ],
[
        InlineKeyboardButton(
            text="Зал 8",
            callback_data="Hall_8_12"
        )
    ],[
        InlineKeyboardButton(
            text="Back",
            callback_data="back_on_sessions_time"
        )
    ]
])