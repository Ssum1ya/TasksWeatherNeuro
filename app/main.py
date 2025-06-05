import asyncio

from aiogram import Bot, Dispatcher

import requests

from databaseTools.WorkWithDb import WorkWithDb
from workTools.WorkWithNeuro import WorkWithNeuro
from workTools.WorkWithWeather import WorkWithWeather
from config import AI_TOKEN, WEATHER_TOKEN, TOKEN

from handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    # asyncio.create_task(send_notifications(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())