from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, JobQueue

TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
LINK_AFILIADO = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"
CATEGORIA = "Ofertas Relâmpago"
INTERVALO_MINUTOS = 5

MENSAGEM = f"""🔥 *{CATEGORIA} Shopee!*

Aproveite agora as melhores promoções com frete grátis e cupons de desconto.

🛍️ [Ver Oferta Agora]({LINK_AFILIADO})

✅ Estoque limitado. Preço pode mudar a qualquer momento!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot de ofertas da Shopee ativado!\nUse /oferta para começar a receber promoções."
    )

async def oferta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if "chats" not in context.application.bot_data:
        context.application.bot_data["chats"] = set()
    context.application.bot_data["chats"].add(chat_id)
    await update.message.reply_text(
        f"🔔 Você receberá *{CATEGORIA}* a cada {INTERVALO_MINUTOS} minutos.",
        parse_mode="Markdown",
    )

async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    chats = context.application.bot_data.get("chats", set())
    for chat_id in chats:
        try:
            await context.bot.send_message(chat_id=chat_id, text=MENSAGEM, parse_mode="Markdown")
        except Exception as e:
            print(f"Erro ao enviar mensagem para {chat_id}: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oferta", oferta))

    # Agenda tarefa periódica com o job_queue do telegram.ext
    job_queue: JobQueue = app.job_queue
    job_queue.run_repeating(enviar_ofertas, interval=INTERVALO_MINUTOS*60, first=10)

    print("🚀 Bot iniciado. Esperando comandos...")
    app.run_polling()

if __name__ == "__main__":
    main()
