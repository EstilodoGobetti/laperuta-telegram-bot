# main.py

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot ativo! Use /start para testar comandos.")

# Criação do bot
app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

# Adicionando o comando /start
app.add_handler(CommandHandler("start", start))

# Inicia o bot
print("🚀 Bot pronto para receber comandos.")
app.run_polling()
