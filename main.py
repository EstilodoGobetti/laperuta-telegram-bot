import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Olá! Bot funcionando! Use /ajuda para ver comandos.")

async def ajuda(update, context):
    msg = (
        "Aqui estão os comandos disponíveis:\n"
        "/start - Inicia o bot\n"
        "/ajuda - Lista de comandos\n"
    )
    await update.message.reply_text(msg)

async def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("Bot rodando!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

   

