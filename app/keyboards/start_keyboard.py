from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Погода", callback_data = 'Weather'), InlineKeyboardButton(text="Вопрос", callback_data = 'Question'), InlineKeyboardButton(text="Задачи", callback_data = 'Tasks')]
])