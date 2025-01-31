import uvicorn
import logging
from fastapi.middleware.cors import CORSMiddleware
from aiogram.types import Update
from app.app import create_app
from bot.handlers.start import dp, bot
from database.base.create import rollout as init_db
from config import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


app = create_app()
host = "0.0.0.0"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WEBHOOK_PATH = f"/bot/{config.BOT_TOKEN}"
WEBHOOK_URL = config.WEBHOOK_URL + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    init_db()


@app.post(WEBHOOK_PATH)
async def webhook(update: dict) -> None:
    logging.info("Received webhook request")
    telegram_update = Update(**update)
    await dp.feed_webhook_update(bot=bot, update=telegram_update)
    logging.info("Update processed")


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()


if __name__ == '__main__':
    uvicorn.run('asgi:app', host=host,  port=5050, log_level='debug')

