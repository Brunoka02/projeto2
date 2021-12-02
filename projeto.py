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

dicionario_erros = {}
for nome in lista_nome_dos_jogadores :
    dicionario_erros.update({nome: 0})

lista_de_mortos = []
for i in range(len(lista_nome_dos_jogadores)):
    lista_de_mortos.append("_")




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

#############################logica do jogo


enforcou = False
acertou = False
erros = 0
aux2=0
contador_dos_erros_totais = 0
erros_maximos = len(lista_nome_dos_jogadores)*6
erros_totais = 0
while(erros_totais != erros_maximos and not acertou):
    



    

    while dicionario_erros[lista_nome_dos_jogadores[aux2]] == 6:
        aux2 += 1
        if aux2 >= int(len(lista_nome_dos_jogadores)):
            aux2 = 0
        
        






    print(lista_dos_caracteres[aux2])
    chute = input("Qual letra {}? ".format(lista_nome_dos_jogadores[aux2]))
    chute = chute.strip().upper()


    if(chute in lista_de_palavras[aux2]):
        index = 0
        for letra in lista_de_palavras[aux2]:
            if(chute == letra):
                lista_dos_caracteres[aux2][index] = letra
            index += 1
    else:
        dicionario_erros[lista_nome_dos_jogadores[aux2]] += 1 
        print("Você já errou {} vezes".format(dicionario_erros[lista_nome_dos_jogadores[aux2]]))
        erros_totais +=1
        
            
        
        



        
    
    if "_" not in lista_dos_caracteres[aux2]:
        acertou = True
        continue
    print(lista_dos_caracteres[aux2])
    aux2 += 1
    if aux2 == len(lista_nome_dos_jogadores):
        aux2 = 0
    input("Aperte ENTER para continuar")
    print("\n"*130)


if acertou:
    print(lista_de_palavras[aux2])
    print("Você venceu {}".format(lista_nome_dos_jogadores[aux2]))
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
else:
    print("Todos erraram")
    print('''\n\n 
    ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
    ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
    █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
    █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
    ███     █    █  ▀███▀               █  █  ▀███▀     █   
            █    ▀                        █▐            ▀    
        ▀                              ▐                  
    ''')


    

