import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Olá! Bot funcionando!")

async def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("Bot rodando!")
    await asyncio.Event().wait()  # Espera para manter o bot ativo

if __name__ == "__main__":
    asyncio.run(main())
