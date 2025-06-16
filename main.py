import os
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Pega o token do bot da variável de ambiente (GitHub Secrets)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá, Estilo do Laperuta! Bot rodando perfeitamente!')

def main():
    # Cria a aplicação do bot com o token
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona o comando /start
    app.add_handler(CommandHandler("start", start))

    # Inicia o bot e mantém rodando até parar manualmente
    app.run_polling()

if __name__ == '__main__':
    main()
