respostas = {
    "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?": "Joan Taylor",
    "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?": "The Undeep",
    "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISODIO?": "Streamberry",
    "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?": "Assistindo a um episódio enquanto estava na cama.",
    "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?": "Joan teve uma reação inicial de desgosto e choque, e decidiu confrontar os produtores do show.",
    "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?": "Perda de privacidade e falta de controle sobre a própria imagem.",
    "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR?": "Sim, com uma reflexão sombria sobre as consequências das tecnologias modernas."
}


pergunta = input("Qual é a sua dúvida? ")
pergunta = pergunta.upper()  # Convertendo a pergunta para maiúsculas

if pergunta in respostas:
    print("Resposta:", respostas[pergunta])
else:
    print("Desculpe, não tenho uma resposta para essa pergunta.")



