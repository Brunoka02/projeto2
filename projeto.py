import random, func, time, forca_animacoes as anima, palavras_dicas as p_dicas

resposta = True

while resposta:
    anima.inicio()

    func.gerar_rank()
    personagem = []
    dicas = []
    silviobot = []
    anima.set_animacoes(personagem, silviobot)
    lista_nome_dos_jogadores = func.função_pedir_nomes()
    palavras_e_dificuldade =  func.função_escolher_dificuldade()
    palavras = palavras_e_dificuldade[0]
    pontuacao = (palavras_e_dificuldade[1]*25)+15
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
    anima.silviobot(silviobot)
    while(erros_totais != erros_maximos and not acertou):
        while dicionario_erros[lista_nome_dos_jogadores[aux2]] == 6:
            aux2 += 1
            if aux2 >= int(len(lista_nome_dos_jogadores)):
                aux2 = 0
        func.limpar()
        print('Patrícia: A pista é', p_dicas.get_dicas(lista_de_palavras[aux2].lower()))
        print('Silviobot: Temos um', p_dicas.get_dicas(lista_de_palavras[aux2].lower()), 'de', len(lista_de_palavras[aux2]),'letras')
        func.converteListaString(lista_dos_caracteres[aux2])
        chute = input("Qual letra ou qual palavra, {}? ".format(lista_nome_dos_jogadores[aux2]))
        while chute.isnumeric():
            print('OPÇÃO INVÁLIDA! Informe uma letra ou uma palavra!')
            chute = input("Qual letra ou qual palavra, {}? ".format(lista_nome_dos_jogadores[aux2]))
        else:
            chute = chute.strip().upper()
        
        if chute == lista_de_palavras[aux2]:
            acertou = True
            continue

        elif(chute in lista_de_palavras[aux2]):
            index = 0
            for letra in lista_de_palavras[aux2]:
                if(chute == letra):
                    lista_dos_caracteres[aux2][index] = letra
                index += 1
            func.slowprint(('Silviobot: Tem, claro que tem, pode marcar letra ' + str(chute)))
        else:
            dicionario_erros[lista_nome_dos_jogadores[aux2]] += 1 
            print("Você já errou {} vez(es)".format(dicionario_erros[lista_nome_dos_jogadores[aux2]]))
            erros_totais +=1
            pontuacao -= 5
            func.limpar()
            func.slowprint('Silviobot: Não, não, não... essa foi furada...')
            time.sleep(1)
            func.desenho_da_forca(dicionario_erros[lista_nome_dos_jogadores[aux2]], personagem, aux2)
        if "_" not in lista_dos_caracteres[aux2]:
            acertou = True
            continue

        func.converteListaString(lista_dos_caracteres[aux2])
        aux2 += 1
        if aux2 == len(lista_nome_dos_jogadores):
            aux2 = 0
        input("Aperte ENTER para continuar")
        func.limpar()

    if acertou:
        func.imprimir_vencedor(lista_de_palavras[aux2],lista_nome_dos_jogadores[aux2])
        print('Você fez', pontuacao, 'pontos.\n')
        input('Tecle ENTER para continuar')
        func.salvar_pontuacao(lista_nome_dos_jogadores[aux2], pontuacao)
        func.gerar_rank()
        func.slowprint('-------------')
        func.slowprint('Hall da Fama:')
        func.slowprint('-------------')
        func.imprimir_podio()
        resposta = func.novoJogo()
    else:
        func.imprimir_todos_erraram()
        resposta = func.novoJogo()
