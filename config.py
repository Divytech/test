import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", 25728264))
    API_HASH = os.getenv("API_HASH", "7716997c3f0ef421c6bc23cd95c640d8")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7666348795:AAFuWdbl8NYRafTXqFR2Mog9A5nEnypKM3U")
    WORK_DIR = os.getenv("WORK_DIR", "./")
