from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Погода", callback_data = 'Weather'), InlineKeyboardButton(text="Вопрос", callback_data = 'Question'), InlineKeyboardButton(text="Задачи", callback_data = 'Tasks')]
])