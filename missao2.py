candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0

while True:
    
    print ('Sistema Eleitoral do Gremio Estudantil: \n1.Novo voto. \n2.Encerrar votos.')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        nome = input ('Digite seu nome:')
        idade = int(input('Digite sua idade: '))

        if idade < 16:
            print (f'Desculpe {nome}, você não possui idade o suficiente!\n')
        else:
            print ('Candidatos:\nCandidato 1.\nCandidato 2.\nCandidato 3.\nCandidato 4.')
            candidato = int(input('Digite o número do seu candidato: '))

            if candidato == 1:
                candidato1 += 1
            elif candidato == 2:
                candidato2 += 1
            elif candidato == 3:
                candidato3 += 1
            else:
                candidato4 += 1
    else:
        break

print (f'Votos computados:\nCandidato 1 recebeu {candidato1} votos.\nCandidato 2 recebeu {candidato2} votos.\nCandidato 3 recebeu {candidato3} votos.\nCandidato 4 recebeu {candidato4} votos.')