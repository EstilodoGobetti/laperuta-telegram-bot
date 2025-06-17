from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
CHAT_ID = 1623073007
LINK_OFERTA = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"

async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text=f"🔥 Oferta Relâmpago Shopee! Confira aqui: {LINK_OFERTA}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot iniciado! Você receberá ofertas a cada 2 minutos.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Registrar comando /start
    app.add_handler(CommandHandler("start", start))

    # Agendar tarefa para enviar ofertas a cada 2 minutos (120 segundos)
    app.job_queue.run_repeating(enviar_ofertas, interval=120, first=10)

    print("Bot iniciado. Enviando ofertas a cada 2 minutos.")
    app.run_polling()

if __name__ == "__main__":
    main()
