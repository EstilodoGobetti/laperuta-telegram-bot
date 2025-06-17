import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Bot ativo e funcionando!")

# Função principal segura para ambientes que já rodam um loop
async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        print("❌ ERRO: Token não definido. Configure a variável TELEGRAM_BOT_TOKEN no Railway.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot pronto para receber comandos.")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.wait_until_shutdown()
    await app.stop()
    await app.shutdown()

# Executa sem usar asyncio.run() diretamente (evita conflito de loop)
try:
    asyncio.get_event_loop().run_until_complete(main())
except RuntimeError as e:
    if "already running" in str(e):
        print("⚠️ Loop já está em execução. Adaptando execução...")
        asyncio.ensure_future(main())
    else:
        raise

