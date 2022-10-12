import telebot

CHAVE_API = "5704009301:AAHjftDPZqG9Bx6-4dWgCipkbiABUFQ9LZ0"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
	bot.send_message(mensagem.chat.id, "Para fazer uma reclamação, envie um e-mail para: banco.reclamacao@banco.com.br")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
	bot.send_message(mensagem.chat.id, "Para tirar seu holerite/extrato, acesse o internet banking no site: www.meubanco/holerite.com.br")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
	bot.send_message(mensagem.chat.id, """
	Capital: 4004-3508
	Interior: 4004-3509
	Demais localidades: 4004-3510""")


@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """
   /agencia1 Agencias na Paulista
	/agencia2 Agencias em Pinheiros
	/agencia3 Agencias em Osasco"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["agencia1"])
def agencia1(mensagem):
	bot.send_message(mensagem.chat.id,"""
	Rua
	Av
	Rua""")

@bot.message_handler(commands=["agencia2"])
def agencia2(mensagem):
    bot.send_message(mensagem.chat.id,"""
	Rua
	Av
	Rua""")

@bot.message_handler(commands=["agencia3"])
def agencia3(mensagem):
	bot.send_message(mensagem.chat.id,"""
	Rua
	Av
	Rua""")

def verificar(mensagem):
    return True
  


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá meu nome é Teozinho, como posso ajudar: (Clique em uma das opções abaixo):
	/opcao1 Fazer uma reclamação
	/opcao2 Quero tirar meu extrato/holerite
	/opcao3 Quero entrar em contato via telefone
	/opcao4 Preciso ir em uma agência
	Caso tente alguma outra opção, não vai funcionar"""
    bot.reply_to(mensagem, texto)




bot.polling()