from aiogram import Router
from aiogram.types import CallbackQuery, Message
from core.keyboards.keyboard_session12 import keyboard_12hr, back_12hr_button,keyboard_12technobis, back_12technobis_button, keyboard_12since, back_12since_button

router = Router()


@router.callback_query(lambda c: c.data == "hr12")
async def hr10(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали HR-территорию.\n"
                                       f"Под это направление работает 2 зала.", reply_markup=keyboard_12hr)


@router.callback_query(lambda c: c.data == "hall1_12hr")
async def send_text12_1(callback: CallbackQuery):
    with open ("core/texts/session12-1.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12hr_button)


@router.callback_query(lambda c: c.data == "hall2_12hr")
async def send_text12_2(callback: CallbackQuery):
    with open ("core/texts/session12-2.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12hr_button)


@router.callback_query(lambda c: c.data == "technobis12")
async def technobis12(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали территорию технологического предпринимательства.\n"
                                       f"Под это направление работает 4 зала.", reply_markup=keyboard_12technobis)


@router.callback_query(lambda c: c.data == "hall3_12hr")
async def send_text12_3(callback: CallbackQuery):
    with open ("core/texts/session12-3.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12technobis_button)


@router.callback_query(lambda c: c.data == "hall4_12hr")
async def send_text12_4(callback: CallbackQuery):
    with open ("core/texts/session12-4.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12technobis_button)


@router.callback_query(lambda c: c.data == "hall5_12hr")
async def send_text12_5(callback: CallbackQuery):
    with open ("core/texts/session12-5.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12technobis_button)


@router.callback_query(lambda c: c.data == "hall6_12hr")
async def send_text12_6(callback: CallbackQuery):
    with open ("core/texts/session12-6.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12technobis_button)


@router.callback_query(lambda c: c.data == "since12")
async def since12(callback: CallbackQuery):
    await callback.message.answer(text=f"Вы выбрали территорию науки, культуры и спорта.\n"
                                       f"Под это направление работает 2 зала.", reply_markup=keyboard_12since)



@router.callback_query(lambda c: c.data == "hall7_12hr")
async def send_text12_7(callback: CallbackQuery):
    with open("core/texts/session12-7.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12since_button)


@router.callback_query(lambda c: c.data == "hall8_12hr")
async def send_text12_8(callback: CallbackQuery):
    with open("core/texts/session12-8.txt", "r") as file:
        text_content = file.read()
    await callback.message.answer(text_content, reply_markup=back_12since_button)