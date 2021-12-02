import random
print("Bem vindo ao")
print('''
     ██╗ ██████╗  ██████╗  ██████╗     ██████╗  █████╗     ███████╗ ██████╗ ██████╗  ██████╗ █████╗ 
     ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
     ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║    █████╗  ██║   ██║██████╔╝██║     ███████║
██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║    ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║
╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║    ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║
 ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                                                    
 ''')

print("Nome dos jogadores: \nPara terminar a escolha de nomes digite CONTINUAR")
pedindo_nomes = True
index = 1
lista_nome_dos_jogadores = []
while pedindo_nomes:
    nome = input("O {} jogador chama: ".format(index))
    if nome.upper()=="CONTINUAR":
        pedindo_nomes = False
        continue
    else:
        lista_nome_dos_jogadores.append(nome)
        index += 1

print("Escolha a dificuldade")
print("FÁCIL[1]\nMÉDIO[2]\nDIFÍCIL[3]")
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
lista_de_palavras = []
for i in range(len(lista_nome_dos_jogadores)):
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    lista_de_palavras.append(palavra_secreta)
print(lista_de_palavras)
#######################################################
lista_dos_caracteres = []
aux = 0
contador = 0
for palavra in range(len(lista_de_palavras)):
    letras_acertadas = ["_" for letra in lista_de_palavras[aux]]
    lista_dos_caracteres.append(letras_acertadas)
    aux +=1
print(lista_dos_caracteres)





    

