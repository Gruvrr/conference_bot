from aiogram import Router
from aiogram.types import CallbackQuery, Message
from core.keyboards.keyboard_session10 import keyboard_10hr, back_10hr_button,keyboard_10technobis, back_10technobis_button, keyboard_10since, back_10since_button

router = Router()


@router.callback_query(lambda c: c.data == "hr10")
async def hr10(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали HR-территорию.\n"
                                       f"Под это направление работает 2 зала.", reply_markup=keyboard_10hr)


@router.callback_query(lambda c: c.data == "hall1_10hr")
async def send_text10_1(callback: CallbackQuery):
    with open ("core/texts/session10-1.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10hr_button)


@router.callback_query(lambda c: c.data == "hall2_10hr")
async def send_text10_2(callback: CallbackQuery):
    with open ("core/texts/session10-2.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10hr_button)


@router.callback_query(lambda c: c.data == "technobis10")
async def technobis10(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали территорию технологического предпринимательства.\n"
                                       f"Под это направление работает 4 зала.", reply_markup=keyboard_10technobis)


@router.callback_query(lambda c: c.data == "hall3_10hr")
async def send_text10_3(callback: CallbackQuery):
    with open ("core/texts/session10-3.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10technobis_button)


@router.callback_query(lambda c: c.data == "hall4_10hr")
async def send_text10_4(callback: CallbackQuery):
    with open ("core/texts/session10-4.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10technobis_button)


@router.callback_query(lambda c: c.data == "hall5_10hr")
async def send_text10_5(callback: CallbackQuery):
    with open ("core/texts/session10-5.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10technobis_button)


@router.callback_query(lambda c: c.data == "hall6_10hr")
async def send_text10_6(callback: CallbackQuery):
    with open ("core/texts/session10-6.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10technobis_button)


@router.callback_query(lambda c: c.data == "since10")
async def technobis10(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали территорию науки, культуры и спорта.\n"
                                       f"Под это направление работает 2 зала.", reply_markup=keyboard_10since)



@router.callback_query(lambda c: c.data == "hall7_10hr")
async def send_text10_7(callback: CallbackQuery):
    with open("core/texts/session10-7.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10since_button)


@router.callback_query(lambda c: c.data == "hall8_10hr")
async def send_text10_8(callback: CallbackQuery):
    with open("core/texts/session10-8.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_10since_button)