import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CHECK_API_URL: str = os.getenv('CHECK_API_URL')
    CHECK_API_TOKEN: str = os.getenv('CHECK_API_TOKEN')
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    WEBHOOK_URL: str = os.getenv('WEBHOOK_URL')
    DB_NAME: str = os.getenv('DB_NAME')


config = Config()
