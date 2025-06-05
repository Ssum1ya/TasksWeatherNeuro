from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.start_keyboard import start
from keyboards.tasks_keyboard import tasks_choose, inline_tasks, task_array, delete_keyboard

from config import AI_TOKEN, WEATHER_TOKEN

from workTools.WorkWithNeuro import WorkWithNeuro
from workTools.WorkWithWeather import WorkWithWeather
from databaseTools.WorkWithDb import WorkWithDb

class Flag(StatesGroup):
    question = State()
    weather = State()
    append_task = State()

delete_task = None

router = Router()
user_message = F.data.split()
path = "C:/Users/Proger/Documents/TasksWeatherNeuro/app/databaseTools/database.json"

@router.message(Command("start", "restart"))
async def command_start(message: Message):
    await message.answer("Выберите задачу:", reply_markup = start)

@router.callback_query(F.data == 'start')
async def callback_start(callback: CallbackQuery):
    await callback.message.edit_text("Выберите задачу:", reply_markup = start)

@router.callback_query(F.data == 'Weather')
async def weather_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Flag.weather)
    await callback.answer('Напишите город', show_alert = True)

@router.message(Flag.weather)
async def question(message: Message, state: FSMContext):
    await state.update_data(weather = message.text)
    await state.clear()
    data = WorkWithWeather.answer(message.text, WEATHER_TOKEN)
    string_answer = ''

    if data != 'Incorrect city':
        temprature = f'Темпрература - {data['temp']} °C, '
        description = f'Погода сегодня - {data['description']}, '
        humidity = f'Влажность - {data['humidity']} %, '
        pressure = f'Давление - {data['pressure']} мм рт. ст., '
        speed = f'Скорость ветра - {data['speed']} м/с, '
        string_answer = temprature + description + humidity + pressure + speed
    else:
        string_answer += 'Неверно введён город'
    await message.answer(string_answer)

@router.callback_query(F.data == 'Question')
async def question_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Flag.question)
    await callback.answer('Напишите вопрос', show_alert = True)

@router.message(Flag.question)
async def question(message: Message, state: FSMContext):
    await state.update_data(question = message.text)
    await state.clear()
    return_answer = await WorkWithNeuro.generate_response(message.text, AI_TOKEN)
    await message.answer(return_answer)


@router.callback_query(F.data == 'Tasks')
async def tasks_start(callback: CallbackQuery):
    await callback.message.edit_text("Выберите задачу:", reply_markup = tasks_choose)

@router.callback_query(F.data == 'append_task')
async def task_writing(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Flag.append_task)
    await callback.answer('Напишите задачу', show_alert = True)

@router.message(Flag.append_task)
async def task_append(message: Message, state: FSMContext):
    await state.update_data(append_taks = message.text)
    await state.clear()
    WorkWithDb.append_task(str(message.chat.id), message.text, path)
    await message.answer('Задача добавлена', show_alert = True)

@router.callback_query(F.data == 'check_tasks')
async def check_tasks(callback: CallbackQuery):
    tasks = WorkWithDb.show_tasks(str(callback.message.chat.id), path)

    await callback.message.edit_text("Ваши задачи", reply_markup = await inline_tasks(tasks))

@router.callback_query(F.data.in_(task_array))
async def deleting_start(callback: CallbackQuery):
    global delete_task
    delete_task = callback.data
    await callback.message.edit_text("Удаление задачи", reply_markup = delete_keyboard)

@router.callback_query(F.data == 'delete')
async def deleting_task(callback: CallbackQuery):
    WorkWithDb.delete_task(str(callback.message.chat.id), delete_task, path)
    await callback.answer('Задача удалена', show_alert = True)
    await callback.message.edit_text("Выберите задачу:", reply_markup = tasks_choose)

@router.callback_query(F.data == 'back_to_choose')
async def back_to_choose(callback: CallbackQuery):
    await callback.message.edit_text("Выберите задачу:", reply_markup = tasks_choose)