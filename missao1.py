Notas = [1.5, 4.0, 6.7, 5.9, 10, 7.1, 3.4]  # As notas foram salvas em um vetor por ordem da chamada

for i in range(len(Notas)):  # Agora os índices vão de 0 a 6, sem erro!
    if Notas[i] >= 6:
        print(f'Aluno {i}: aprovado')
    else:
        print(f'Aluno {i}: reprovado')