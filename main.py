import os
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Olá! Bot funcionando!")

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("Erro: TELEGRAM_BOT_TOKEN não está definido nas variáveis de ambiente!")
        return
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

