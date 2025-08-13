import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# گرفتن Token از Environment Variable
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Bot Token پیدا نشد! مطمئن شو Environment Variable با نام BOT_TOKEN ست شده.")

# یک دستور ساده /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! بات شما با موفقیت اجرا شد 😎")

# ساخت Application
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن Handler
app.add_handler(CommandHandler("start", start))

# اجرا کردن بات
if __name__ == "__main__":
    print("بات در حال اجراست...")
    app.run_polling()
