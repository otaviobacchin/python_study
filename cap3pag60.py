#Exercício 3.4
print('Exercício 3.4')
salario = 1000.00
imposto = (salario >=1200.00)
print(imposto)

#Exercício 3.5
print('\nExercício 3.5')
print('Exemplo 1')
a = 1
b = 2
c = True
d = False
resultado = (a>b and c or d)
print(resultado)

print('\nExemplo 2')
a = 10
b = 3
c = False
d = False
resultado = (a>b and c or d)
print(resultado)

print('\nExemplo 3')
a = 5
b = 1
c = True
d = True
resultado = (a>b and c or d)
print(resultado)

#Exercício 3.6
print('\nExercício 3.6')
materia1 = 8
materia2 = 9
materia3 = 10
media = 7
aprovado = (materia1 >= media and materia2 >= media and materia3 >= media)
print(aprovado)