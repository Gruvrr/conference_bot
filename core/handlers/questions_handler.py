from aiogram.types import CallbackQuery
from core.keyboards.back_button import back


async def question_1(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}!\n"
                                       f"Подача заявок на участие в Конгрессе \n"
                                       f"проводится участниками самостоятельно \n"
                                       f"посредством заполнения регистрационной формы \n"
                                       f"на официальном сайте мероприятия: \n"
                                       f"https://scienceplusbusiness.ru/ ", reply_markup=back)
    await callback.answer()


async def question_2(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}! До 8 декабря на указанную при регистрации"
                                       f"электронную почту и в Телеграм Вам придет письмо-подтверждение.", reply_markup=back)
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
                                       f"Начало регистрации: 09:00. \n"
                                       f"Регистрация на Конгресс проводится при наличии паспорта. \n"
                                       f"Схемы проезда и парковки доступны на сайте: \n"
                                       f"https://scienceplusbusiness.ru/contacts. \n"
                                       f"Также актуальная информация о мероприятии \n"
                                       f"будет доступна в этом чат-боте ", reply_markup=back)
    await callback.answer()

async def question_5(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}! \n"
                                       f"Подробная информация об аккредитации СМИ представлена \n"
                                       f"на сайте мероприятия: https://scienceplusbusiness.ru/ \n"
                                       f"в разделе «Пресс-центр»", reply_markup=back)
    await callback.answer()


async def question_6(callback: CallbackQuery):
    name = callback.from_user.first_name
    await callback.message.answer(text=f"Добрый день, {name}.\n"
                                       f"Уточните, пожалуйста, ваши фамилию, имя, отчество. \n"
                                       f"В ближайшее время на почту, указанную при регистрации, или Телеграм, \n"
                                       f"будет выслано письмо-подтверждение вашей регистрации в системе. \n"
                                       f"Если подобное письмо не поступит, просим Вас еще раз заполнить заявку до 4 декабря ", reply_markup=back)
    await callback.answer()