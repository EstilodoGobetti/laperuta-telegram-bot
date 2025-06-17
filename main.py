import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bot rodando direitinho 🚀")

async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")  # Pega o token do ambiente

    if not token:
        print("ERRO: A variável TELEGRAM_BOT_TOKEN não está definida!")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    # Executa a corrotina sem usar asyncio.run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
