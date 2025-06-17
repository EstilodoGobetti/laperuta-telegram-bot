import requests
from bs4 import BeautifulSoup
from telegram.ext import ApplicationBuilder, JobQueue
import asyncio

TOKEN = '8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk'
CHAT_ID = 1623073007
SHOPEE_OFFERS_URL = 'https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1'

async def enviar_ofertas(context):
    try:
        response = requests.get(SHOPEE_OFFERS_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Exemplo básico para pegar nomes e links — ajustar conforme estrutura da Shopee
        produtos = soup.find_all('a', href=True)  # Pega todos links, filtrar depois

        mensagem = '🔥 Ofertas Relâmpago Shopee 🔥\n\n'
        count = 0

        for produto in produtos:
            href = produto['href']
            if '/product/' in href or '/item/' in href:  # Filtros simples para links de produto
                nome = produto.get_text(strip=True)
                if not nome:
                    continue

                link_completo = 'https://shopee.com.br' + href

                mensagem += f"{nome}\n{link_completo}\n\n"
                count += 1
                if count >= 5:
                    break

        if count == 0:
            mensagem = 'Nenhuma oferta relâmpago encontrada no momento.'

        await context.bot.send_message(chat_id=CHAT_ID, text=mensagem)

    except Exception as e:
        print(f"Erro ao enviar ofertas: {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    job_queue: JobQueue = app.job_queue

    job_queue.run_repeating(enviar_ofertas, interval=120, first=10)  # 2 minutos

    print("Bot iniciado. Enviando ofertas a cada 2 minutos.")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
