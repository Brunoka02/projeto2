
import random

def função_pedir_nomes():
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
    return lista_nome_dos_jogadores



def função_escolher_dificuldade():
    print("Escolha a dificuldade")
    print("FÁCIL-Comidas-[1]\nMÉDIO-Eletrodomesticos-[2]\nDIFÍCIL-Programação-[3]")
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
    return palavras


def sortear_palavras(lista_nome_dos_jogadores,palavras):
    lista_de_palavras = []
    for i in range(len(lista_nome_dos_jogadores)):
        numero = random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()
        lista_de_palavras.append(palavra_secreta)
    return lista_de_palavras



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
        print("A palavra era ",palavra)
        print("Você venceu {}".format(vencedor))
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


def desenho_da_forca(numero_erros):
    if numero_erros == 1:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (O_O) 
 ||            
 ||       
 ||      
 ||       
 ||      
 ||
 ||      
----------------
''')
    if numero_erros == 2:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (O_O) 
 ||          | | 
 ||          | |
 ||          | |
 ||       
 ||
 ||
 ||      
---------------- 
''')
    if numero_erros == 3:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (O_O) 
 ||        //| | 
 ||       // | |
 ||          | |
 ||       
 ||      
 ||
 ||      
----------------
''')
    if numero_erros == 4:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (O_O) 
 ||        //| |\\\\
 ||       // | | \\\\
 ||          | |
 ||       
 ||
 ||
 ||      
----------------     
 
''')

    if numero_erros == 5:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (0_0) 
 ||        //| |\\\\
 ||       // | | \\\\
 ||          | |
 ||         //
 ||        //
 ||
 ||      
---------------- 
''')

    if numero_erros == 6:
        print(''' 


 _______________
 |____________|_|
 ||           |
 ||         (x_x) 
 ||        //| |\\\\
 ||       || | | ||
 ||          | |
 ||         // \\\\
 ||        //   \\\\
 ||
 ||      
---------------- 
''')

