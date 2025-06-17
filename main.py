import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue
import logging

# CONFIGURAÇÕES FIXAS
TOKEN = "7875891498:AAHEmRJRUqXQrxnMZrrxqj-zN2J7BwwzUOQ"  # Seu token do bot
CHAT_ID = "-1002120685101"  # ID do canal ou grupo
INTERVALO_MINUTOS = 2  # Tempo entre mensagens

# ATIVAR LOGS
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot do Laperuta ativo com ofertas automáticas!")

# Mensagem de oferta automática
async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🔥 Oferta Relâmpago na Amazon!\n\n"
        "💪 *Colágeno Tipo 2 Premium + Cálcio + Magnésio* – ideal para suas articulações!\n\n"
        "🛒 Aproveite aqui 👉 [Ver na Amazon](https://amzn.to/4ktiC8y)\n\n"
        "🚚 Entrega rápida | ✅ Produto bem avaliado | 💰 Preço especial por tempo limitado"
    )

    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=mensagem,
        parse_mode="Markdown"
    )

# Função principal
async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    job_queue: JobQueue = app.job_queue
    job_queue.run_repeating(enviar_ofertas, interval=INTERVALO_MINUTOS * 60, first=10)

    logger.info("🚀 Bot iniciado no Railway com envio a cada 2 minutos.")
    await app.run_polling()

# Execução segura
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e).startswith("This event loop is already running"):
            import nest_asyncio
            nest_asyncio.apply()
            asyncio.get_event_loop().run_until_complete(main())
        else:
            raise
