import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bot funcionando!")

async def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("Token do bot não encontrado. Verifique se a variável de ambiente TELEGRAM_BOT_TOKEN está definida.")
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    await app.initialize()
    await app.start()
    print("Bot rodando no Railway! ✅")
    await asyncio.Event().wait()  # Mantém o bot rodando

if __name__ == "__main__":
    asyncio.run(main())
print("Bot atualizado!")
