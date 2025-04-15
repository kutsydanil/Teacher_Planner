import asyncio
import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

logger = logging.getLogger(__name__)
main_router = Router()

def get_main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📅 Сегодня"),
                KeyboardButton(text="📆 Завтра"),
                KeyboardButton(text="🗓 Неделя")
            ],
            [
                KeyboardButton(text="⚙️ Настройки"),
                KeyboardButton(text="🆘 Помощь")
            ],
            [
                KeyboardButton(text="ℹ️ О боте")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )

@main_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать! Используйте меню:",
        reply_markup=get_main_menu()
    )

@main_router.message(F.text == "📅 Сегодня")
async def handle_today(message: types.Message):
    await message.answer("⌛️ События на сегодня в разработке...")

@main_router.message(F.text == "📆 Завтра")
async def handle_tomorrow(message: types.Message):
    await message.answer("⌛️ События на завтра в разработке...")

@main_router.message(F.text == "🗓 Неделя")
async def handle_week(message: types.Message):
    await message.answer("⌛️ События на неделю в разработке...")

@main_router.message(F.text == "⚙️ Настройки")
async def handle_settings(message: types.Message):
    await message.answer("⚙️ Раздел настроек в разработке...")

@main_router.message(F.text == "🆘 Помощь")
async def handle_help(message: types.Message):
    await message.answer("ℹ️ Справка по боту в разработке...")

@main_router.message(F.text == "ℹ️ О боте")
async def handle_about(message: types.Message):
    about_text = (
        "🤖 <b>Умный планировщик для преподавателей</b>\n\n"
        "Основные возможности:\n"
        "• Просмотр расписания на день/неделю\n"
        "• Управление событиями Google Calendar\n"
        "• Настраиваемые напоминания\n"
        "• Интеграция с Zoom/Google Meet\n\n"
        "Версия: 1.0\n"
        "Разработчик: Шух-интерпрайс"
    )
    await message.answer(about_text, parse_mode="HTML")

    

async def main():
    load_dotenv()
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(main_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())