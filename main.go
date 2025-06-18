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

// Função que faz scraping (exemplo básico)
// Você deve trocar o seletor e a URL para o produto que quer monitorar
func buscarDados() (string, string, error) {
	url := "https://shopee.com.br/product/12345678/1234567890" // Troque para o URL do produto real

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

// Função que envia mensagem para Telegram
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

// Job que será executado nos horários programados
func job(token, chatID string) {
	log.Println("Executando job de atualização")

	preco, img, err := buscarDados()
	if err != nil {
		log.Println("Erro no scraping:", err)
		return
	}

	linkProduto := "https://s.shopee.com.br/2LMb6NCr2p?share_channel_code=1" // seu link de afiliado

	msg := fmt.Sprintf("🔥 *Produto Shopee*\nPreço Atual: %s\n[Veja o produto aqui](%s)\n\nImagem: %s", preco, linkProduto, img)

	err = enviarTelegram(msg, token, chatID)
	if err != nil {
		log.Println("Erro ao enviar Telegram:", err)
	} else {
		log.Println("Mensagem enviada com sucesso!")
	}
}

func main() {
	token := "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
	chatID := "1623073007"

	// Usando horário de Brasília (UTC-3)
	c := cron.New(cron.WithLocation(time.FixedZone("BRT", -3*3600)))

	horarios := []string{
		"0 0 * * *",  // 00:00
		"0 9 * * *",  // 09:00
		"0 12 * * *", // 12:00
		"0 16 * * *", // 16:00
		"0 18 * * *", // 18:00
		"0 20 * * *", // 20:00
		"0 22 * * *", // 22:00
	}

	for _, h := range horarios {
		_, err := c.AddFunc(h, func() {
			job(token, chatID)
		})
		if err != nil {
			log.Println("Erro ao agendar horário:", h, err)
		}
	}

	c.Start()
	log.Println("Bot iniciado e aguardando horários agendados...")

	select {} // Mantém o programa rodando
}
