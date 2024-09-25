# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0


a = 0
b = 0
lista =[]

for c in range (5):
    num = float(input("Digite a nota do aluno: "))

    lista.append(num)

    print(lista)
    a+=num
    b+=num
    if b > 0:
        media = a/b



print(f"Maior nota: {max(lista)}")
print(f"Menor nota : {min(lista)}")
print('Média : {}'.format(media))