# Trabalhando com índices

# Programa 6.3 - Apresentação de Números:

numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f'Número {x + 1}: '))
    x += 1
while True:
    escolhido = int(input('Que posição você quer imprimir (0 para sair): '))
    if escolhido == 0:
        break
    print(f'Você escolheu o número: {numeros[escolhido - 1]}')

# Cópia e fatiamento de listas:

# Quando copiamos uma lista e tentamos modificar o valor de um conteúdo da lista duplicada, ambas as listas são modificadas:

L = [1, 2, 3, 4, 5]
V = L
print ('\nExemplo de cópias de listas 1:')
print (f'Lista L = {L}')
print (f'Lista V = {V}')

V[0] = 6

print ('\nModificando o valor de V[0], ambas as listas mudam:')
print (f'Lista L = {L}')
print (f'Lista V = {V}')

# Ao modificarmos a lista V, modificamos também o conteúdo de L. Isso porque uma lista em Python é um objeto e, quando atribuímos um objeto a outro, estamos apenas copiando a mesma
# referência da lista, e não seus dados em si. Nesse caso, V funciona como um apelido de L, ou seja, V e L são a mesma lista. Quando modificamos V[0] estamos modificando também L[0].

# Para criar uma cópia da lista, utilizamos uma sintaxe [:]

L = [1, 2, 3, 4, 5]
V = L[:]
V[0] = 6
print ('\nExemplo de cópias de listas 2:')
print (f'Lista L = {L}')
print (f'Lista V = {V}')

# Podemos também fatiar uma lista, da mesma forma que fizemos com os strings no cap3:

print ('\nExemplos de "fatiamento" de listas:')
L = [1, 2, 3, 4, 5]
print(L[0:5]) #Lista do elemento 0 ao 5
print(L[:5]) #Lista do elemento inicial ao 5
print(L[:-1]) #Lista até antes do último elemento
print(L[1:3]) #Lista do elemento 1 ao 2
print(L[1:4]) #Lista do elemento 2 ao 3
print(L[3:]) #Lista do elemento 4 pra cima
print(L[:3]) #Lista do início até o 3 elemento
print(L[-1]) #Mostra o último elemento
print(L[-2]) #Mostra o penúltimo elemento