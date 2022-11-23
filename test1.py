import telebot

CHAVE_API = "5777576439:AAG_ymxZCf4PXZJcjgZHv7HBeglIyaUXsU4"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["reclamacao"])
def reclamacao(mensagem):
	bot.send_message(mensagem.chat.id, "Para fazer uma reclamação, envie um e-mail para: banco.reclamacao@banco.com.br")

@bot.message_handler(commands=["Extrato"])
def extrato(mensagem):
	bot.send_message(mensagem.chat.id, "Para tirar seu holerite/extrato, acesse o internet banking no site: www.meubanco/holerite.com.br")

@bot.message_handler(commands=["Atendente"])
def atendente(mensagem):
    bot.send_message(mensagem.chat.id, "Caso seu problema não esteja em uma das opções mencionadas, clique no link para ser direcionada para um atendente -- ")    
    

@bot.message_handler(commands=["Contatos"])
def contatos(mensagem):
	bot.send_message(mensagem.chat.id, """
	Capital: 4004-3508
	Interior: 4004-3509
	Demais localidades: 4004-3510""")
 

@bot.message_handler(commands=["Agencias"])
def agencias(mensagem):
    texto = """
 	/Paulista Agencias na Paulista
	/Pinheiros Agencias em Pinheiros
	/Osasco Agencias em Osasco"""
    bot.send_message(mensagem.chat.id, texto)
    
  
@bot.message_handler(commands=["Paulista"])
def paulista(mensagem):
	bot.send_message(mensagem.chat.id,"""
 	Av. Paulista 901, 16° andar, São Paulo, SP
    Maps: https://goo.gl/maps/2cxvkThxwiSeMiBEA "
 	""")

@bot.message_handler(commands=["Pinheiros"])
def pinheiros(mensagem):
    bot.send_message(mensagem.chat.id,"""
 	Rua Teodoro Sampaio 1600, São Paulo, SP, 05406-100
	Maps: https://goo.gl/maps/iZT9d9yQ8RvA7VCj8
	""")

@bot.message_handler(commands=["Osasco"])
def osasco(mensagem):
	bot.send_message(mensagem.chat.id,"""
	Rua Antonio Agu 860, Osasco, SP
	Maps: https://goo.gl/maps/Kqv3Aqw9vR1HMvmm9
	""")

def verificar(mensagem):
    return True
  


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá meu nome é Teozinho, como posso ajudar: (Clique em uma das opções abaixo):
	/Reclamacao Quero fazer uma reclamação
	/Extrato Quero tirar meu extrato/holerite
	/Contatos Quero entrar em contato via telefone
	/Atendente Quero falar com um atendente
	/Agencias Preciso ir em uma agência
	Caso tente alguma outra opção, não vai funcionar"""
    bot.reply_to(mensagem, texto)




bot.polling()