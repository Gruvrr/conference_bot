from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from core.keyboards import keyboard_session10, back_button
from core.keyboards.keyboard_session10 import territory_keyboards10
from core.keyboards.keyboard_session12 import territory_keyboards12

router = Router()


@router.callback_query(lambda c: c.data == "back_on_time")
async def choice_session(callback: CallbackQuery):
    await callback.message.answer(text="Выберете интересующее вас время.", reply_markup=keyboard_session10.keyboard_time)
    await callback.answer()


@router.callback_query(lambda c: c.data == "10")
async def choice_time_10(callback: CallbackQuery):
    await callback.message.answer(text=f"Первая сессия начинается в 10 часов.\n"
                                       f"Для вашего удобства мы разделили залы по территориям.\n"
                                       f"Выберете интересующее вас территорию", reply_markup=territory_keyboards10)
    await callback.answer()


@router.callback_query(lambda c: c.data == "12")
async def choice_time_12(callback: CallbackQuery):
    await callback.message.answer(text=f"Вторая сессия начинается в 12 часов.\n"
                                       f"Для вашего удобства мы разделили залы по территориям.\n"
                                       f" Выберете интересующее вас территорию", reply_markup=territory_keyboards12)
    await callback.answer()


@router.callback_query(lambda c: c.data == "14")
async def choice_time_15(callback: CallbackQuery):
    time = "14:00 – 16:00"
    event_title = "Пленарное заседание: «Совокупный суверенитет 2.0: эффективные пути взаимодействия науки, бизнеса, культуры и власти»"
    moderator = "Наталья Попова, первый заместитель генерального директора компании «Иннопрактика»"
    description = (
        "На IX Конгрессе «Инновационная практика: наука плюс бизнес» участники пришли к выводу о том, что в новых условиях "
        "необходимо сделать ставку на достижение совокупного суверенитета страны в технологической, информационной, культурной "
        "и других важных для общества и экономики областях. Сегодня в рамках пленарного заседания X Конгресса планируется "
        "актуализировать прошлогоднюю тему, определив понятие «совокупный суверенитет России» с учетом накопленных за этот год опыта и"
    )
    formatted_text = f"{time}\n\n{event_title}\n\nМодератор: {moderator}\n\nОписание:\n\n{description}"

    await callback.message.answer(text=formatted_text, reply_markup=back_button.back_on_sessions_time)
    await callback.answer()


