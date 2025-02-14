while True:
    
    print ('\nSistema de Nota escolar \n1.Verificar classificação da Nota \n2.Sair.')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        nome = input ('Digite seu nome:')
        nota = float(input('Digite sua nota: '))

        if nota >= 90.0 and nota <= 100.0:
            print ("Parabéns, você tirou A!")
        elif nota < 90 and nota >= 80:
            print ("Muito bem, você tirou B.")
        elif nota >= 70 and nota < 70:
            print ("Bom trabalho, você tirou C.")
        elif nota >= 60 and nota < 70:
            print ("Fique atento, você tirou D.")
        elif nota >= 0 and nota < 60:
            print ("Estude um pouco mais, você tirou F.")
        else:
            print ("nota invalida")

    elif opcao == 2:
        break

    else:
        print ("Opção invalida!")

print ("\nSistema encerrado!")