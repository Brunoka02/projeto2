import random
import func
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

lista_nome_dos_jogadores = func.função_pedir_nomes()
palavras =  func.função_escolher_dificuldade()
dicionario_erros = {}
for nome in lista_nome_dos_jogadores :
    dicionario_erros.update({nome: 0})
lista_de_palavras = func.sortear_palavras(lista_nome_dos_jogadores,palavras)
lista_dos_caracteres = func.criar_lista_caracteres(lista_de_palavras)

#parte do jogo

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
    chute = input("Qual letra ou palavra {}? ".format(lista_nome_dos_jogadores[aux2]))
    chute = chute.strip().upper()
    if chute == lista_de_palavras[aux2]:
        acertou = True
        continue

    elif(chute.upper() in lista_de_palavras[aux2]):
        index = 0
        for letra in lista_de_palavras[aux2]:
            if(chute == letra):
                lista_dos_caracteres[aux2][index] = letra
            index += 1
    else:
        dicionario_erros[lista_nome_dos_jogadores[aux2]] += 1 
        print("Você já errou {} vezes".format(dicionario_erros[lista_nome_dos_jogadores[aux2]]))
        erros_totais +=1
        func.desenho_da_forca(dicionario_erros[lista_nome_dos_jogadores[aux2]])
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
    func.imprimir_vencedor(lista_de_palavras[aux2],lista_nome_dos_jogadores[aux2])
else:
    func.imprimir_todos_erraram()


    

