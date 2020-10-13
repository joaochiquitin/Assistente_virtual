import speech_recognition as sr
import pyttsx3

from random import choice
from config import *

reproducao = pyttsx3.init()

def reproduzirSom(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def assistente():

    print("Oi, qual é o seu nome completo?")
    reproduzirSom("Oi, qual é o seu nome completo?")

    while True:
        reposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as microphone:
            rec.adjust_for_ambient_noise(microphone)

            while True:

                try:
                    audio = rec.listen(microphone)
                    user_name = rec.recognize_google(audio, language="pt")
                    user_name = verificar_nome(user_name)

                    name_list()

                    apresentacao = "{}".format(verifica_existe_nome(user_name))
                    print(apresentacao)
                    reproduzirSom(apresentacao)

                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]

                    break

                except sr.UnknownValueError:
                    reproduzirSom(reposta_erro_aleatoria)

            break

    print("=" * len(apresentacao))
    print("Ouvindo...")

    while True:
        reposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as microphone:
            rec.adjust_for_ambient_noise(microphone)

            while True:

                try:
                    audio = rec.listen(microphone)
                    entrada = rec.recognize_google(audio, language="pt")

                    print("{}: {}".format(user_name, entrada))

                    #Abrir link no navegador
                    if "abrir" in entrada or "Abrir" in entrada:
                        resposta = abrir(entrada)

                    #Operações matematicas

                    elif "quanto é" in entrada or "Quanto é" in entrada:
                        
                        entrada = entrada.replace("quanto é", "")
                        entrada = entrada.replace("Quanto é", "")
                        
                        resposta = calcular(entrada)

                    #Temperatura atual, etc..
                    elif "qual a temperatura" in entrada or "Qual a temperatura" in entrada:
                        
                        lista_tempo = temperatura()
                        temp = lista_tempo[0]
                        temp_max = lista_tempo[1]
                        temp_min = lista_tempo[2]

                        resposta = "A temperatura de hoje é: {:.2f}°. Temos uma máxima de {:.2f}° e uma mínima de {:.2f}°".format(temp, temp_max, temp_min)

                    #Informações sobre a cidade
                    elif "informações" in entrada and "cidade" in entrada:
                        resposta = "Mostrando informações da cidade"

                    else:
                        resposta = conversas[entrada]

                    if resposta == "Mostrando informações da cidade":
                        lista_info = clima_tempo()

                        longitude = lista_info[0]
                        latitude = lista_info[1]
                        temp = lista_info[2]
                        temperatura_maxima =  lista_info[3]
                        temperatura_minima = lista_info[4]
                        pressao_atm = lista_info[5]
                        humidade = lista_info[6]
                        velocidade_vento = lista_info[7]
                        direcao_vento = lista_info[8]
                        nebulosidade = lista_info[9]
                        id_da_cidade = lista_info[10]

                        print("Assistente: ")
                        print("\nMostrando informações de {}\n".format(cidade))
                        reproduzirSom("Mostrando informações de {}".format(cidade))

                        print("Longitude: {}, latitude: {}".format(longitude, latitude))
                        print("Temperatura: {:.2f}°".format(temp))
                        print("Temperatura máxima: {:.2f}°".format(temp_max))
                        print("Temperatura_mínima: {:.2f}°".format(temp_min))
                        print("Humidade do ar: {}".format(humidade))
                        print("Nebulosidade: {}".format(nebulosidade))
                        print("Velocidade do vento: {}m/s\ndireção do vento {}".format(velocidade_vento, direcao_vento))
                    else:
                        print("Assistente: {}".format(resposta))
                        reproduzirSom("{}".format(resposta))

                except sr.UnknownValueError:
                    reproduzirSom(reposta_erro_aleatoria)
                except KeyError:
                    pass


if __name__ == "__main__":
    intro()
    reproduzirSom("Iniciando...")
    assistente()