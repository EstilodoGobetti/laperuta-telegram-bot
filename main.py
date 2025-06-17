import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! 🤖 O bot está funcionando perfeitamente!")

# Função principal
async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("❌ ERRO: A variável de ambiente TELEGRAM_BOT_TOKEN não está definida!")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot iniciado com sucesso. Esperando comandos...")
    await app.run_polling()

# Início
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
