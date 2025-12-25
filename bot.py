from pyrogram import Client, idle
from config import Config
import os

# Create the client
app = Client(
    "convert_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    if not os.path.exists(Config.WORK_DIR):
        os.makedirs(Config.WORK_DIR)
        
    print("Starting Bot...")
    app.start()
    print("Bot Started! Idle now...")
    idle()
    app.stop()
