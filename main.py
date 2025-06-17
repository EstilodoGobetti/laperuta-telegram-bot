import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Bot ativo e funcionando!")

async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("❌ ERRO: TELEGRAM_BOT_TOKEN não configurado no Railway!")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot pronto para receber comandos.")
    await app.run_polling()

# Rodando de forma compatível com Railway
import asyncio
asyncio.run(main())
