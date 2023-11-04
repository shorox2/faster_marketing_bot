from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('ikb', 'action')

def get_start_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Контактная информация'))
    kb.add(KeyboardButton('Отзывы выпускникoв'))

    return kb

ikb_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вперед ➡️", callback_data=cb.new('next_02'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data=cb.new('exit'))]
])

ikb_two = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_01')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_03'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_three = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_02')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_04'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_four = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_03')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_05'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_five = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_04')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_06'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_six = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_05')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_07'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_sev = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_06')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_08'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_eig = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_07')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_09'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_nin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_08')), InlineKeyboardButton(text='Вперед ➡️', callback_data=cb.new('next_10'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

ikb_ten = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад', callback_data=cb.new('back_09'))],
    [InlineKeyboardButton(text='Закрыть каталог', callback_data= cb.new('exit'))]
])

