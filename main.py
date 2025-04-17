from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os
TOKEN = os.environ.get("7282248867:AAFevE-HJ9dOup6n5UooBkwnnCTahIAbxfU")

BOT_TOKEN = '7282248867:AAFevE-HJ9dOup6n5UooBkwnnCTahIAbxfU'

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    file = None

    if message.document:
        file = await message.document.get_file()
    elif message.photo:
        file = await message.photo[-1].get_file()
    elif message.video:
        file = await message.video.get_file()
    elif message.audio:
        file = await message.audio.get_file()
    elif message.voice:
        file = await message.voice.get_file()
    elif message.sticker:
        file = await message.sticker.get_file()

    if file:
        await message.reply_text(f"✅ لینک دانلود فایل:\n{file.file_path}")
    else:
        await message.reply_text("⚠️ لطفاً یک فایل (عکس، ویدیو، داکیومنت و...) بفرست یا فوروارد کن.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_file))
    print("🤖 ربات راه‌اندازی شد...")
    app.run_polling()
