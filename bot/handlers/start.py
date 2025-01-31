from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram import Dispatcher
from bot.enums import StaticMessages
from bot.states import States
from bot.utils import process_code
from database.db_controllers import get_user_by_id
from config import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    user_authorised = get_user_by_id(message.from_user.id)
    if not user_authorised:
        await state.clear()
        await message.answer(StaticMessages.UNKNOWN_MESSAGE)
    else:
        msg = StaticMessages.ACCESS_GRANTED_MESSAGE
        await state.set_state(States.enter_imei)
        await message.answer(msg)


@dp.message(States.enter_imei)
async def enter_code_handler(message: Message) -> None:
    result = await process_code(message.text)
    await message.answer(result)
