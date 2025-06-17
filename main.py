from telegram.ext import ApplicationBuilder, ContextTypes
import logging

TOKEN = "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
CHAT_ID = 1623073007
LINK_AFILIADO = "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def enviar_ofertas(ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_message(
        chat_id=CHAT_ID,
        text=(
            "🔥 *Ofertas‑relâmpago Shopee!* 🔥\n\n"
            f"Acesse 👉 {LINK_AFILIADO}\n\n"
            "Não perca tempo!"
        ),
        parse_mode="Markdown"
    )

async def error_handler(update, ctx):
    logging.error("Erro inesperado", exc_info=ctx.error)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # 🡆 MATA QUALQUER WEBHOOK/SSESSÃO PENDENTE
    app.bot.delete_webhook(drop_pending_updates=True)

    # job a cada 2 min
    app.job_queue.run_repeating(enviar_ofertas, interval=120, first=10)

    app.add_error_handler(error_handler)

    print("Bot no ar – enviando ofertas a cada 2 min.")
    app.run_polling()

if __name__ == "__main__":
    main()
