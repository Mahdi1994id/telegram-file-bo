import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("TOKEN")  # توکن رو از محیط بخون

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! فایل بفرست تا لینکشو بدم 👌")

def handle_file(update: Update, context: CallbackContext):
    try:
        file = update.message.document or update.message.video or update.message.audio or update.message.photo[-1]
        file_id = file.file_id
        file_obj = context.bot.get_file(file_id)
        download_link = f"https://api.telegram.org/file/bot{context.bot.token}/{file_obj.file_path}"
        update.message.reply_text(f"🔗 لینک دانلود مستقیم:\n{download_link}")
    except Exception as e:
        print(f"Error: {e}")
        update.message.reply_text("❌ خطایی در دریافت لینک پیش اومد.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document | Filters.video | Filters.audio | Filters.photo, handle_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
