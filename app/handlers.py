from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.start_keyboard import start

from config import AI_TOKEN, WEATHER_TOKEN

from workTools.WorkWithNeuro import WorkWithNeuro
from workTools.WorkWithWeather import WorkWithWeather

class Flag(StatesGroup):
    question = State()
    weather = State()


router = Router()
user_message = F.data.split()

@router.message(Command("start", "restart"))
async def command_start(message: Message):
    await message.answer("Выберите задачу:", reply_markup = start)

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
    await message.answer(WorkWithNeuro.answer(message.text, AI_TOKEN))