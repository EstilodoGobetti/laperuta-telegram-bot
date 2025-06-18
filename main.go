package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
	"time"

	"github.com/gocolly/colly/v2"
	"github.com/robfig/cron/v3"
)

func buscarDados() (string, string, error) {
	url := "https://shopee.com.br/product/12345678/1234567890" // Troque para o URL real do produto

	c := colly.NewCollector()

	var preco string
	var imgURL string

	c.OnHTML("div._3n5NQx", func(e *colly.HTMLElement) {
		preco = e.Text
	})

	c.OnHTML("img._396cs4", func(e *colly.HTMLElement) {
		src := e.Attr("src")
		if strings.HasPrefix(src, "//") {
			src = "https:" + src
		}
		imgURL = src
	})

	c.OnRequest(func(r *colly.Request) {
		log.Println("Visitando", r.URL.String())
	})

	err := c.Visit(url)
	if err != nil {
		return "", "", err
	}

	if preco == "" || imgURL == "" {
		return "", "", fmt.Errorf("erro ao capturar dados")
	}

	return preco, imgURL, nil
}

func enviarTelegram(mensagem string, token string, chatID string) error {
	url := fmt.Sprintf("https://api.telegram.org/bot%s/sendMessage", token)

	resp, err := http.PostForm(url, map[string][]string{
		"chat_id":    {chatID},
		"text":       {mensagem},
		"parse_mode": {"Markdown"},
	})
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		return fmt.Errorf("falha ao enviar mensagem, status: %d", resp.StatusCode)
	}

	return nil
}

func job(token, chatID string) {
	log.Println("Executando job de atualização")

	preco, img, err := buscarDados()
	if err != nil {
		log.Println("Erro no scraping:", err)
		return
	}

	linkProduto := "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1"

	msg := fmt.Sprintf("🔥 *Produto Shopee*\n\nPreço Atual: %s\n\n[👉 Ver na Shopee](%s)", preco, linkProduto)

	err = enviarTelegram(msg, token, chatID)
	if err != nil {
		log.Println("Erro ao enviar Telegram:", err)
	} else {
		log.Println("Mensagem enviada com sucesso!")
	}
}

func main() {
	token := "SEU_TOKEN_AQUI8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
	chatID := " 1623073007"

	c := cron.New(cron.WithLocation(time.FixedZone("BRT", -3*3600)))

	horarios := []string{
		"0 0 * * *",  // 00:00
		"0 9 * * *",  // 09:00
		"0 12 * * *", // 12:00
		"0 15 * * *", // 15:00
		"0 18 * * *", // 18:00
		"0 21 * * *", // 21:00
	}

	for _, h := range horarios {
		_, err := c.AddFunc(h, func() {
			job(token, chatID)
		})
		if err != nil {
			log.Println("Erro ao agendar tarefa:", err)
		}
	}

	c.Start()

	select {} // bloqueia o programa para ele continuar rodando
}
