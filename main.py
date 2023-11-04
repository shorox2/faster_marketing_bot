from aiogram import types, Dispatcher, executor, Bot
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from keyboards import *

async def on_startup(_):
    print('WIN!')


# storage = MemoryStorage()
bot = Bot(token=TOKEN_API,
          parse_mode='HTML')
dp = Dispatcher(bot=bot)




# @dp.message_handler(content_types=['photo'])
# async def start_cmd(message: types.Message):
#     await message.answer(message)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEKrthlRjw7nra3atrCxVryMOGtp09d1gACBQADwDZPE_lqX5qCa011MwQ')
    await bot.send_photo(chat_id=message.chat.id,
                         photo='AgACAgIAAxkBAAMHZUUNASNo-MMB-KnhGRinPwMhSH8AAoTSMRs_sShKdXrPQ42AmPYBAAMCAANzAAMzBA',
                         caption='\n'.join(CAPTION),
                         reply_markup=get_start_kb())
    await message.delete()

@dp.message_handler(Text(equals='Контактная информация'))
async def contact_cmd(message: types.Message):
    await message.answer(text='\n'.join(TEXT))

@dp.message_handler(Text(equals='Отзывы выпускникoв'))
async def otzivi_cmd(message: types.Message):
    global count
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photos[0][1],
                         caption=photos[0][0],
                         reply_markup=ikb_one)


@dp.callback_query_handler()
async def lisen_keyboard(callback: types.CallbackQuery):

    if callback.data == 'ikb:exit':
        await callback.message.delete()
        await callback.answer()
    elif 'next' in callback.data:
        index = int(callback.data[-2:])
        if '02' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_two)
        elif '03' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_three)
        elif '04' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_four)
        elif '05' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_five)
        elif '06' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_six)
        elif '07' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_sev)
        elif '08' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_eig)
        elif '09' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_nin)
        elif '10' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_ten)

    elif 'back' in callback.data:
        index = int(callback.data[-2:])
        if '02' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_two)
        elif '03' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_three)
        elif '04' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_four)
        elif '05' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_five)
        elif '06' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_six)
        elif '07' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_sev)
        elif '08' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_eig)
        elif '09' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_nin)
        elif '01' in callback.data:
            await callback.message.edit_media(types.InputMedia(media=photos[index-1][1],
                                                        type='photo',
                                                        caption=photos[index-1][0]),
                                      reply_markup=ikb_one)

    await callback.answer()





if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)