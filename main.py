from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot funcionando perfeitamente!")

# Cole seu token do BotFather aqui, entre aspas
TOKEN = "8133241514:AAGhvnBb1uXQzR1J33_EpyL_LBxuCNmZjoE"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🚀 Bot iniciado...")
app.run_polling()
