import asyncio
from telegram.ext import ApplicationBuilder, ContextTypes

TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
CHAT_ID = 1623073007
LINK_AFILIADO = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"

async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    texto = f"🔥 Confira as ofertas relâmpago da Shopee! 🔥\n\nAcesse aqui 👉 {LINK_AFILIADO}\n\nNão perca tempo!"
    await context.bot.send_message(chat_id=CHAT_ID, text=texto)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Limpa updates pendentes para evitar conflito
    await app.bot.get_updates(offset=-1)

    # Agenda envio de ofertas a cada 2 minutos
    app.job_queue.run_repeating(enviar_ofertas, interval=120, first=10)

    print("Bot iniciado. Enviando ofertas a cada 2 minutos.")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
