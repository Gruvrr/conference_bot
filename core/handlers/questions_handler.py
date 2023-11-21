from aiogram.types import CallbackQuery
from core.keyboards.back_button import back


async def question_1(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}!\n"
                                       f"Вы можете самостоятельно зарегистрироваться на официальном сайте мероприятия https://scienceplusbusiness.ru/2023", reply_markup=back)
    await callback.answer()


async def question_2(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}. C 8 по 12 декабря на указанную при регистрации "
                                       f"электронную почту Вам придет письмо-подтверждение.", reply_markup=back)
    await callback.answer()


async def question_3(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}! \n"
                                       f"К сожалению, мы не можем подтвердить Ваше участие \n"
                                       f"в 10-м Конгрессе «Инновационная практика: наука плюс бизнес».\n"
                                       f"В связи с огромным количеством заявок на участие \n"
                                       f"в мероприятии в этом году и бесплатным форматом \n"
                                       f"проведения, мы отдаем приоритет тем, кто зарегистрировался раньше."
                                       f"Благодарим Вас за понимание и интерес, проявленный к мероприятию."
                                       f"Будем рады видеть Вас на других наших мероприятиях!"
                                       f"В случае возникновения вопросов Вы можете написать \n"
                                       f"нам на congress@scienceplusbusiness.ru", reply_markup=back)
    await callback.answer()


async def question_4(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}.\n"
                                       f"10-ый Конгресс «Инновационная практика: наука плюс бизнес» \n"
                                       f"состоится 13 декабря 2023 года \n"
                                       f"в «Хаятт Ридженси Москва Петровский Парк». \n"
                                       f"Начало регистрации: 09:30. \n"
                                       f"Для входа вам необходимо будет предъявить паспорт. \n"
                                       f"Схемы проезда и парковки доступны на сайте: \n"
                                       f"https://scienceplusbusiness.ru/2023#contacts. \n"
                                       f"Также актуальная информация о мероприятии \n"
                                       f"будет доступна в этом чат-боте. ", reply_markup=back)
    await callback.answer()

async def question_5(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}! \n"
                                       f"Подробная информация об аккредитации СМИ будет представлена \n"
                                       f"на сайте мероприятия: https://scienceplusbusiness.ru/ \n"
                                       f"в разделе «Пресс-центр», в начале декабря.", reply_markup=back)
    await callback.answer()


async def question_6(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}.\n"
                                       f"Просим вас направить запрос на congress@scienceplusbusiness.ru, "
                                       f"мы проверим вашу заявку системе и ответим в ближайшее время. Спасибо.", reply_markup=back)
    await callback.answer()