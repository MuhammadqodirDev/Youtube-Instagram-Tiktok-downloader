import os

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests import delete
from loader import dp, bot
from tiktok import tk
# from instagram import instadownloader
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
# from pytube import YouTube
from .start import check_user, CHANNEL_ID, link_menu
from instagram import instadownloader
from pytube import YouTube
from tiktok_instagram_youtube import yt, tk_ins
from .database import create_url


youtube_urls = ['https://www.youtube.com/', "https://youtu.be/", 'https://m.youtube.com/']
other_urls = ["https://www.instagram.com/", 'https://www.tiktok.com']

async def return_buttons(link, message, bot, msg):
    try:
        await bot.delete_message(message.chat.id, msg.message_id)
        datas = []
        if any(link.startswith(item) for item in youtube_urls):
            datas = yt(link)['datas']
        
        elif any(link.startswith(item) for item in other_urls):
            datas = tk_ins(link)['datas']
        else:
            return None

        markup = InlineKeyboardMarkup()

        for i in datas:
            extension = 'Audio' if i['extension'] == 'mp3' else "Video"
            quanlity = i['quality']
            url = i['url']
            id = create_url(url)
            display = f"{extension} - {quanlity}"
            action = f"send_audio_{url}" if i['extension'] == 'mp3' else f"send_video_{id}"
            markup.add(InlineKeyboardButton(f"{display}", callback_data=action))
        
        await bot.send_message(message.chat.id, 'Video sifatini tanlang', reply_markup=markup)
        # return markup

    except Exception as e:
        await bot.send_message(message.chat.id, '❌')
        print(e)
        return None


# @check_user
# @dp.message_handler(Text(startswith='https://www.tiktok.com'))
# async def test(message:types.Message):
#     if not check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
#         await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
#     else:
#         chat_id = message.chat.id
#         msg = await bot.send_message(chat_id, "⌛️")
#         natija = tk(message.text)
#         await message.answer_audio(natija['video'])
#         await bot.delete_message(chat_id, msg.message_id)
#         await bot.delete_message(chat_id, message.message_id)


# # @check_user
# @dp.message_handler(Text(startswith='https://www.instagram.com/'))
# async def send_media(message:types.Message):
#     if not check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
#         await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
#     else:
#         chat_id = message.chat.id
#         link1 = message.text
#         msg = await bot.send_message(chat_id, "⌛️")
#         data = instadownloader(link1=link1)
#         if data == "Error":
#             await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')
#         else:
#             if data['type'] == 'image':
#                 await message.answer_photo(photo=data['media'])
#                 await bot.delete_message(chat_id, msg.message_id)
#             elif data['type'] == 'video':
#                 await message.answer_video(video=data['media'])
#                 await bot.delete_message(chat_id, msg.message_id)
#             elif data['type'] == 'carousel':
#                 for i in data['media']:
#                     await message.answer_document(document=i)
#                 await bot.delete_message(chat_id, msg.message_id)
#             else:

#                 await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')

#             await bot.delete_message(chat_id, message.message_id)



# @dp.message_handler()
# # @check_user
# async def test_mesage(message:types.Message):
#     if not check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
#         await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
#     else:
#         chat_id = message.chat.id
#         url = message.text
#         yt = YouTube(url)
#         if message.text.startswith == 'https://youtu.be/' or 'https"//www.youtube.com/' or 'https://m.youtube.com/':
#             msg = await bot.send_message(chat_id, "⌛️")
#             await download_youtube_video(url, message, bot)
#             await bot.delete_message(chat_id, msg.message_id)
#             await bot.delete_message(chat_id, message.message_id)



async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        # btn = InlineKeyboardMarkup(inline_keyboard=[
        #         [InlineKeyboardButton(text="Musiqasini yuklab olish", callback_data = "btn_1")]
        # ])
        await bot.send_video(message.chat.id, video, caption=f"{yt.title}")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


# async def download_instagram_tiktok(url, message, bot):




@dp.message_handler()
# @check_user
async def answer_message(message:types.Message):
    if not check_user(await dp.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=link_menu)
    else:
        chat_id = message.chat.id
        url = message.text
        # yt = YouTube(url)
        if any(message.text.startswith(item) for item in youtube_urls) or any(message.text.startswith(item) for item in other_urls):
        # if message.text.startswith == 'https://youtu.be/' or 'https"//www.youtube.com/' or 'https://m.youtube.com/':
            msg = await bot.send_message(chat_id, "⌛️")
            buttons = await return_buttons(url, message, bot, msg)
            # await bot.delete_message(chat_id, msg.message_id)
            # await bot.delete_message(chat_id, message.message_id)
