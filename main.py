import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bot rodando direitinho 🚀")

async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        print("ERRO: A variável TELEGRAM_BOT_TOKEN não está definida!")
        return
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    # Usa create_task se já houver loop rodando
    asyncio.get_running_loop().create_task(app.run_polling())

# Detecta se está dentro de ambiente async (como o Railway)
try:
    loop = asyncio.get_running_loop()
    loop.create_task(main())
except RuntimeError:
    # Se nenhum loop estiver rodando, roda normalmente
    asyncio.run(main())
