from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Substitua pelo seu token do BotFather
TOKEN = "8133241514:AAGhvnBb1uXQzR1J33_EpyL_LBxuCNmZjoE"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Seu bot está funcionando com sucesso!")

# Inicialização do bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
