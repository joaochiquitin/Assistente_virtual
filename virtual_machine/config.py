import requests as rq
import webbrowser as web

version = "1.5.0"
cidade = "Naviraí"

def intro():
    mensagem = "Assistente - versão {} / feito por: João Pedro".format(version)
    print("-" * len(mensagem) + "\n{}\n".format(mensagem) + "-" * len(mensagem))

lista_erros = [
    "Tendi foi nada, repete cara",
    "Repita novamente mano",
    "Não entendi, repita cara"
]

conversas = {
    "Olá": "Oi, tudo bem?",
    "sim e você": "Estou bem obrigado",
}

comandos = {
    "desligar": "Desligando...",
    "reiniciar": "Reiniciando..."
}

def verificar_nome(user_name):
    if user_name.startswith("Meu nome é"):
        user_name = user_name.replace("Meu nome é", "")
    if user_name.startswith("Eu me chamo"):
        user_name = user_name.replace("Eu me chamo", "")
    if user_name.startswith("Eu sou o"):
        user_name = user_name.replace("Eu sou o", "")
    if user_name.startswith("Eu sou a"):
        user_name = user_name.replace("Eu sou a", "")

    return user_name

def verifica_existe_nome(nome):
    dados = open("dados/nomes.txt", "r")
    nome_list = dados.readlines()

    if not nome_list:
        vazio = open("dados/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))

        vazio = open("dados/nomes.txt", "w")
        vazio.writelines(conteudo)
        vazio.close()

        return "Olá {}, prazer em te conhecer".format(nome)

    for linha in nome_list:
        if linha == nome:
            return "Olá {}, acho que já nos conhecemos".format(nome)

    vazio = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))

    vazio = open("dados/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close()

    return "Oi {}, é a primeira vez que nos falamos".format(nome)

def name_list():
    try:
        nomes = open("dados/nomes.txt", "r")
        nomes.close()

    except FileNotFoundError:
        nomes = open("dados/nomes.txt", "w")
        nomes.close()

def calcular(entrada):
	if "mais" in entrada or "+" in entrada:
		# É soma
		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) + int(entradas_recebidas[3])

	elif "menos" in entrada or "-" in entrada:
		# É subtração

		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) - int(entradas_recebidas[3])

	elif "vezes" in entrada or "x" in entrada:
		# É vezes

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) * float(entradas_recebidas[3]), 2)

	elif "dividido" in entrada or "/" in entrada:
		# É divisão

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) / float(entradas_recebidas[4]), 2)

	else:

		resultado = "Operação não encontrada"


	return resultado


def clima_tempo():
    endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=bbf986b67851b3408b49131eb021623f&q="
    url = endereco_api + cidade

    info = rq.get(url).json()

    #coordenadas
    longitude = info['coord']['lon']
    latitude = info['coord']['lat']

    #tempo e clima
    temperatura = info['main']['temp'] - 273.15 #Kelvin para celsius
    pressao_atm = info['main']['pressure'] / 1013.25 #Libras para ATM
    humidade = info['main']['humidity']
    temperatura_maxima = info['main']['temp_max'] - 273.15 #Kelvin para celsius
    temperatura_minima = info['main']['temp_min'] - 273.15 #Kelvin para celsius

    #vento
    velocidade_vento = info['wind']['speed']
    direcao_vento = info['wind']['deg']

    #nuvens
    nebulosidade = info['clouds']['all']

    #id
    id_da_cidade = info['id']

    return [longitude, latitude, temperatura, 
        temperatura_maxima, temperatura_minima,
        pressao_atm, humidade, velocidade_vento,
        direcao_vento, nebulosidade, id_da_cidade]

def temperatura():
    temperatura_atual = clima_tempo()[2]
    temperatura_maxima = clima_tempo()[3]
    temperatura_minima = clima_tempo()[4]

    return [temperatura_atual, temperatura_maxima, temperatura_minima]

def abrir(fala):
    try:
        if "google" in fala or "Google" in fala:
            web.open_new_tab('https://www.google.com/')
            return "Abrindo Google..."

        elif "facebook" in fala or "Facebook" in fala:
            web.open_new_tab('https://www.facebook.com/')
            return "Abrindo Facebook..."
        
        else:
            return "Site não cadastrado para ser aberto"

    except:
        return "Houve um erro!"