from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Coloque seu token aqui
TOKEN = '8133241514:AAGhvnBb1uXQzR1J33_EpyL_LBxuCNmZjoE'

# Função que responde ao comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Bot funcionando!')

async def main():
    # Cria a aplicação do bot com o token
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona o handler do comando /start
    app.add_handler(CommandHandler("start", start))

    # Inicia o bot e fica aguardando mensagens
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
