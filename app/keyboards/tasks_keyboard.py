from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

tasks_choose = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Посмотреть задачи", callback_data = 'check_tasks'),
    InlineKeyboardButton(text="Добавить задачу", callback_data = 'append_task'),
    InlineKeyboardButton(text="Назад", callback_data = 'start')]
])

task_array = []

delete_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Удалить", callback_data = 'delete'), InlineKeyboardButton(text="Назад", callback_data = 'check_tasks')]
])

async def inline_tasks(tasks):
    keyboard = InlineKeyboardBuilder()
    task_array.clear()
    for task in tasks:
        task_array.append(task)
        keyboard.add(InlineKeyboardButton(text = task, callback_data = task))
    keyboard.add(InlineKeyboardButton(text = 'Назад', callback_data = 'back_to_choose'))
    return keyboard.adjust(3).as_markup()