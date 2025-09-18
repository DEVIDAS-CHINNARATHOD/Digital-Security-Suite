import os
import asyncio
from dotenv import load_dotenv
import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext._jobqueue import JobQueue

# Fix timezone issue for Python 3.13
JobQueue._DEFAULT_TIMEZONE = pytz.utc

# Load bot token from .env
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /show to display the Captured Data.")

# /show command
async def show_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("dist/text.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        await update.message.reply_text("text.txt file not found.")
        return

    chat_id = update.effective_chat.id

    for line in lines:
        clean_line = line.strip()
        if clean_line:
            await context.bot.send_message(chat_id=chat_id, text=clean_line)
            await asyncio.sleep(0.5)  # delay between lines

# Start the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("show", show_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
