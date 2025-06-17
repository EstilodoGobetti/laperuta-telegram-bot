from telegram.ext import ApplicationBuilder, ContextTypes
import logging

# ======= SEUS DADOS ========
TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
CHAT_ID = 1623073007
LINK_AFILIADO = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"
# ============================

# Configurar log para ver erros
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):
    texto = (
        f"🔥 Confira as ofertas relâmpago da Shopee! 🔥\n\n"
        f"Acesse aqui 👉 {LINK_AFILIADO}\n\n"
        "Não perca tempo!"
    )
    await context.bot.send_message(chat_id=CHAT_ID, text=texto)

async def error_handler(update, context):
    logging.error("Ocorreu um erro:", exc_info=context.error)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Limpar webhook (caso tenha)
    app.bot.delete_webhook()

    # Agenda enviar mensagem a cada 2 minutos (120 segundos)
    app.job_queue.run_repeating(enviar_ofertas, interval=120, first=10)

    # Adicionar manipulador de erros para registrar exceções
    app.add_error_handler(error_handler)

    print("Bot iniciado. Enviando ofertas a cada 2 minutos.")
    app.run_polling()

if __name__ == "__main__":
    main()
