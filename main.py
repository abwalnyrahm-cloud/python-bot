from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا! أنا بوت الأمن السيبراني.\n"
      
    )
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tips", tips))

    print("Bot is running...")
    app.run_polling()
