# Capítulo 6 - Listas, dicionários, tuplas e conjuntos.

# Programa 6.1 - Cálculo da média:

notas = [6, 7, 8, 7, 9]
soma = 0
n_notas = 0
while n_notas < 5:
    soma += notas[n_notas]
    n_notas += 1
print(f'A média é {soma / n_notas:.2f}\n    ')

# Exercício 6.1 - Modifique o programa para inserir e ler 7 notas. 

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
n_notas = 0
ordem = 1
while n_notas < 7:
    notas[n_notas] = float(input(f'Digite a {ordem}° nota: '))
    soma += notas[n_notas]
    n_notas += 1
    ordem += 1
print(f'A média das notas é {soma / n_notas:.2f}\n')

# Extra: Adicionar nome das matérias no programa.

notas = [0, 0, 0, 0, 0, 0, 0]
materias = ['Ciências', 'Geografia', 'História', 'Matemática', 'Física', 'Química', 'Gramática']
soma = 0
n_notas = 0
while n_notas < 7:
    notas[n_notas] = float(input(f'Digite a nota de {materias[n_notas]}: '))
    soma += notas[n_notas]
    n_notas += 1
print(f'A média das notas é {soma / n_notas:.2f}\n')