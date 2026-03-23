from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT = os.getenv("TOKEN_TELEGRAM")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.effective_message.id,"Здарова")



app = ApplicationBuilder().token(TOKEN_BOT).build()

app.add_handler(CommandHandler("hello",hello))

app.run_polling()

