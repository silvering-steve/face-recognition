import os
from dotenv import load_dotenv

load_dotenv()

APP_HOST=os.getenv("APP_HOST")
APP_PORT=int(os.getenv("APP_PORT"))

APP_STAGE = True if os.getenv("APP_STAGE") == "DEV" else False