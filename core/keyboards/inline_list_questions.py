from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


fac = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Как зарегистрироваться на мероприятие?",
            callback_data="question_1"
        )
    ],
    [
        InlineKeyboardButton(
            text="Когда придет подтверждение?",
            callback_data="question_2"
        )
    ],
    # [
    #     InlineKeyboardButton(
    #         text="Письмо-подтверждение моего участия в мероприятии так и не пришло.",
    #         callback_data="question_3"
    #     )
    # ],
    [
        InlineKeyboardButton(
            text="Где и во сколько состоится мероприятие?",
            callback_data="question_4"
        )
    ],[
        InlineKeyboardButton(
            text="Как можно аккредитоваться в качестве СМИ?",
            callback_data="question_5"
        )
    ],
    [
        InlineKeyboardButton(
            text="Прошу проверить наличие моей заявки",
            callback_data="question_6"
        )
    ],
[
        InlineKeyboardButton(
            text="Назад",
            callback_data="click_back_in_main_menu"
        )
    ]
])