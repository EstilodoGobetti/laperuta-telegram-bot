func main() {
	// Token e chat ID fixos no código
	token := "8113927737:AAHKFPdD7M-9XuP44NpZrt1AcpUM0bFxolk"
	chatID := "1623073007"

	c := cron.New(cron.WithLocation(time.FixedZone("BRT", -3*3600)))

	horarios := []string{
		"0 0 * * *",   // 00:00
		"0 9 * * *",   // 09:00
		"0 12 * * *",  // 12:00
		"0 16 * * *",  // 16:00
		"0 18 * * *",  // 18:00
		"0 20 * * *",  // 20:00
		"0 22 * * *",  // 22:00
	}

	for _, spec := range horarios {
		_, err := c.AddFunc(spec, func() {
			job(token, chatID)
		})
		if err != nil {
			log.Fatal("Erro ao agendar:", err)
		}
	}

	log.Println("Bot iniciado e agendado para rodar nos horários definidos")
	c.Start()

	select {}
}
