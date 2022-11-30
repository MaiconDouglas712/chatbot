import telebot

CHAVE_API = "5617557285:AAF6NROSa3CDTGfTf65k7FFWSZX_naCFt2A"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["Reclamacao"])
def reclamacao(mensagem):
	bot.send_message(mensagem.chat.id, "Para fazer uma reclamação, envie um e-mail para: techzone.reclamacao@banco.com.br")


@bot.message_handler(commands=["Extrato"])
def extrato(mensagem):
	bot.send_message(mensagem.chat.id, "Para tirar seu holerite/extrato, acesse o internet banking no site: https://leomendes475.github.io/Techzone/extrato.html")

@bot.message_handler(commands=["Atendente"])
def atendente(mensagem):
    bot.send_message(mensagem.chat.id, "Um atendente irá entrar em contato no número cadastrado")    
    

@bot.message_handler(commands=["Site"])
def site(mensagem):
	bot.send_message(mensagem.chat.id, """
	Para acessar o site do banco, clique no link ao lado -- https://leomendes475.github.io/Techzone/""")
 
 
@bot.message_handler(commands=["Boleto"])
def bolet(mensagem):
	bot.send_message(mensagem.chat.id, """
	Para retirar a 2 via do seu boleto acesso o link ao lado -- https://leomendes475.github.io/Techzone/segunda-via-boleto.html""")
 

@bot.message_handler(commands=["Agencias"])
def agencias(mensagem):
    texto = """
 	/Paulista Agencias na Paulista
	/Pinheiros Agencias em Pinheiros
	/Osasco Agencias em Osasco"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["PerdiCartao"])
def perdiCartao(mensagem):
    texto = """
    Seu cartão será bloqueado e um novo será enviado ao seu endereço! """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["CartaoAdicional"])
def cartaoAdicional(mensagem):
    texto = """
    Seu cartão adicional será enviado no endereço cadastrado! """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Emprestimo"])
def emprestimo(mensagem):
    texto = """
    Seu prefil será avaliado e em 8 horas enviaremos ao e-mail cadastrado a resposta da avaliação """
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
    Olá meu nome é Teozinho, em que posso ajudar: (Clique em uma das opções abaixo):
    
	/Reclamacao Quero fazer uma reclamação
 
	/Extrato Quero tirar meu extrato/holerite
 
	/Site Quero acessar o site do banco
 
	/Atendente Quero falar com um atendente
 
	/Agencias Preciso ir em uma agência
 
	/PerdiCartao Perdi meu cartão de débito
    
	/CartaoAdicional Pedir cartão adicional
 
	/Emprestimo Pedir emprestimo
 
	/Boleto Segunda via do boleto
 
	Caso tente alguma outra coisa, infelizmente não irá funciona!"""
    bot.reply_to(mensagem, texto)


bot.polling()