
import random
import time
import os
import forca_animacoes as anima
import sys

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./80)

def função_pedir_nomes():
    pedindo_nomes = True
    index = 1
    lista_nome_dos_jogadores = []
    while pedindo_nomes:
        nome = input("O jogador {} chama: ".format(index))
        if nome.upper()=="CONTINUAR":
            if len(lista_nome_dos_jogadores) < 2:
                print("Só é permitido jogar com 2(dois) ou mais jogadores!")
                pedindo_nomes = True
                continue
            else:
                pedindo_nomes = False
                continue
        elif nome.upper()=="RANK":
            imprimir_podio()
        else:
            lista_nome_dos_jogadores.append(nome)
            index += 1

        
    return lista_nome_dos_jogadores

def função_escolher_dificuldade():
    slowprint("-------------------------------------------------\nEscolha a dificuldade: \n")
    slowprint("FÁCIL-[1]\nMÉDIO-[2]\nDIFÍCIL-[3]\nObs: Digite a opção e tecle enter\n")
    dificuldade = int(input())

    if dificuldade == 1:
        arquivo = open("palavras_faceis.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    elif dificuldade == 2:
        arquivo = open("palavras_medias.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    else:
        arquivo = open("palavras_dificeis.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    return (palavras, dificuldade)


def sortear_palavras(lista_nome_dos_jogadores,palavras):
    lista_de_palavras = []
    for i in range(len(lista_nome_dos_jogadores)):
        numero = random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()
        lista_de_palavras.append(palavra_secreta)
    return lista_de_palavras

def get_dicas():
    arquivo2 = open("dicas.txt", "r")
    dicas = []
    for linha in arquivo2:
        linha = linha.strip()
        dicas.append(linha)

    arquivo2.close()
    novo = []
    for x in dicas:
        item = x
        for y in ['\n', '\t', '/', '.', '-', '(', ')']:
            item = item.replace(y, "")
        novo.append(item)
    return dicas

def criar_lista_caracteres(lista_de_palavras):
    lista_dos_caracteres = []
    aux = 0
    contador = 0
    for palavra in range(len(lista_de_palavras)):
        letras_acertadas = ["_" for letra in lista_de_palavras[aux]]
        lista_dos_caracteres.append(letras_acertadas)
        aux +=1
    return lista_dos_caracteres

def imprimir_vencedor(palavra, vencedor):
    limpar()
    print("A palavra era {}.".format(palavra))
    time.sleep(1)
    print("Você venceu, {}!".format(vencedor))
    time.sleep(1)
    print('''\n\n 
        
    /$$$$$$$                              /$$                                    
    | $$__  $$                            | $$                                    
    | $$  \ $$ /$$$$$$   /$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$
    | $$$$$$$/|____  $$ /$$__  $$|____  $$| $$__  $$ /$$__  $$| $$__  $$ /$$_____/
    | $$____/  /$$$$$$$| $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ 
    | $$      /$$__  $$| $$      /$$__  $$| $$  | $$| $$_____/| $$  | $$ \____  $$
    | $$     |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/
    |__/      \_______/|__/      \_______/|_______/  \_______/|__/  |__/|_______/ 
                                                                                
        ''')


def imprimir_todos_erraram():
    limpar()
    slowprint("Todos erraram")
    time.sleep(1)
    print('''\n\n 
        ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
        ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
        █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
        █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
        ███     █    █  ▀███▀               █  █  ▀███▀     █   
                █    ▀                        █▐            ▀    
            ▀                              ▐                  
        ''')


def desenho_da_forca(numero_erros, personagem, aux2):
    if numero_erros == 1:
        if aux2%2 == 0:
            anima.cinco_vidas_restantesp1(personagem)
        else:
            anima.cinco_vidas_restantesp2(personagem)
    if numero_erros == 2:
        if aux2%2 == 0:
            anima.quatro_vidas_restantesp1(personagem)
        else:
            anima.quatro_vidas_restantesp2(personagem)
    if numero_erros == 3:
        if aux2%2 == 0:
            anima.tres_vidas_restantesp1(personagem)
        else:
            anima.tres_vidas_restantesp2(personagem)
    if numero_erros == 4:
        if aux2%2 == 0:
            anima.duas_vidas_restantesp1(personagem)
        else:
            anima.duas_vidas_restantesp2(personagem)

    if numero_erros == 5:
        if aux2%2 == 0:
            anima.uma_vida_restantep1(personagem)
        else:
            anima.uma_vida_restantep2(personagem)

    if numero_erros == 6:
        if aux2%2 == 0:
            anima.gameoveranimacaop1(personagem)
        else:
            anima.gameoveranimacaop2(personagem)

def replacer(lista):
    novo = []
    for x in lista:
        item = x
        for y in ['\n', '\t', '/', '.', '-', '(', ')']:
            item = item.replace(y, "")
        novo.append(item)
    return novo

def salvar_pontuacao(jogador, pontuacao):
    with open('nomes.txt', 'a') as f:
        f.writelines(str(jogador) + '\n')
        f.close()
    with open('pontos.txt', 'a') as f:
        f.writelines(str(pontuacao) + '\n')
        f.close()
    return

def gerador_rank(lista_nomes, lista_pontuacoes):
    return sorted(list(zip(lista_pontuacoes, lista_nomes)))[::-1]

def gerar_rank():
    with open('pontos.txt') as f:
        lines2 = f.readlines()
        f.close()
    with open('nomes.txt') as f:
        lines = f.readlines()
        f.close()
    lines = replacer(lines)
    lines2 = replacer(lines2)
    rank = gerador_rank(lines, lines2)
    with open('rank.txt', 'w') as f:
        for i in range(0, len(rank)):
            f.writelines(str(i+1) + '-' + ' '+ str(rank[i]) + '\n')
        f.close()

def imprimir_podio():
    with open('rank.txt') as f:
        lines = f.readlines()
    replacer(lines)
    i = 0
    while i != 3:
        print(lines[i])
        i += 1
    return 
    
def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)

def converteListaString(lista):
    palavra = ''

    for caracter in lista:
        palavra = palavra + caracter.upper()

    print(palavra)
