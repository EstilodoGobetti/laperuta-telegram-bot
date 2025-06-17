import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
LINK_AFILIADO = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"
INTERVALO_MINUTOS = 5

MENSAGEM = f"""🔥 *Ofertas Relâmpago Shopee!*

Confira agora as melhores promoções.

🛍️ [Clique aqui e aproveite]({LINK_AFILIADO})

Estoque limitado!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, o bot está funcionando!")

async def oferta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if "chats" not in context.application.bot_data:
        context.application.bot_data["chats"] = set()
    context.application.bot_data["chats"].add(chat_id)
    await update.message.reply_text(f"Você receberá ofertas a cada {INTERVALO_MINUTOS} minutos.")

async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    chats = context.application.bot_data.get("chats", set())
    for chat_id in chats:
        try:
            await context.bot.send_message(chat_id=chat_id, text=MENSAGEM, parse_mode="Markdown")
        except Exception as e:
            print(f"Erro ao enviar para {chat_id}: {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oferta", oferta))

    # Agenda o job para enviar ofertas
    app.job_queue.run_repeating(enviar_ofertas, interval=INTERVALO_MINUTOS * 60, first=10)

    print("Bot rodando...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # Aguarda até ser encerrado (ctrl+c)
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Railway já roda um loop, então rodamos main direto no loop atual
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())




   
