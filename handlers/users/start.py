from email import message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from .database import create_user
CHANNEL_IDS = ['@nimadir_uchun']

from .database import get_url_by_id


import tracemalloc
tracemalloc.start()

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")


link_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text="➕ A'zo bo'lish", url='https://t.me/nimadir_uchun'),
        InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='check_user')
    ]
])


async def check_user(message, user_id=None):
    if not user_id:
        user_id = message.from_user.id
    for CHANNEL_ID in CHANNEL_IDS:
        chat_member = await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if chat_member['status'] not in ["left","kicked"]:
            pass
        else:
            await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
            return False
    return True

    # if message.chat.type == 'private':
    #     if check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
    #         await dp.bot.send_message(message.from_user.id, text="Video kochirish uchun link yuborishingiz mumkin")
    #     else:
    #         await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
            
    # if chat_member['status'] != 'left':
    #     # await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=ink_menu)
    #     return True
    # else:
    #     return False


# @check_user
@dp.message_handler(CommandStart())
# @dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    msg = await message.reply("Salom 😊, bu bot orqali Youtube, Instagram va Tiktok videolarini yuklab olishingiz mumkin!")
    res = await check_user(message)
    try:
        create_user(message.from_user.id)
    except Exception as e:
        print(e)
    if res:
        await dp.bot.send_message(message.from_user.id, text="Video kochirish uchun link yuborishingiz mumkin")
    # if message.chat.type == 'private':
    #     if check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
    #     else:
    #         await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)


@dp.callback_query_handler(lambda c: c.data == 'check_user')
async def start_button(call:types.CallbackQuery):
    query = call.data
    chat_id = call.message.chat.id
    if query == "check_user":
        # data = await dp.bot.get_chat_member(chat_id=CHANNEL_ID,user_id=chat_id)
        # if data.status in ["left","kicked"]:
        res = await check_user(call.message, user_id=call.from_user.id)
        if res == False:
            await dp.bot.delete_message(call.from_user.id, call.message.message_id)
            await call.answer("Kechirasiz siz kanalga a'zo bo'lmadingiz",show_alert=True)
        else:
            await call.message.delete()
            await dp.bot.send_message(chat_id=chat_id,text="Video kochirish uchun link yuborishingiz mumkin")

@dp.callback_query_handler(lambda c: c.data.startswith("send_"))
async def send_datas(call:types.CallbackQuery):
    await dp.bot.delete_message(call.from_user.id, call.message.message_id)
    # if check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)):
    #     pass
    #     # await dp.bot.send_message(call.from_user.id, text="Video kochirish uchun link yuborishingiz mumkin")
    # else:
    #     await dp.bot.send_message(call.from_user.id, f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {call.from_user.full_name}!", reply_markup=link_menu)

    chat_id = call.message.chat.id
    type, url_id = call.data.replace('send_', '').split('_')

    url = get_url_by_id(url_id)

    await call.answer('')
    try:
        if type == 'video':
            print(url)
            await dp.bot.send_video(chat_id, url)
        elif type == 'audio':
            await dp.bot.send_audio(chat_id, url)
        else:
            raise Exception('xatolik')
    except Exception as e:
        print(e)
        await dp.bot.send_message(chat_id=chat_id,text='❌')
    
    # query = call.data
    # if query == "check_user":
    #     data = await dp.bot.get_chat_member(chat_id=CHANNEL_ID,user_id=chat_id)
    #     if data.status in ["left","kicked"]:
    #         await call.answer("Kechirasiz siz kanalga a'zo bo'lmadingiz",show_alert=True)
    #     else:
    #         await call.message.delete()
    #         await dp.bot.send_message(chat_id=chat_id,text="Video kochirish uchun link yuborishingiz mumkin")


