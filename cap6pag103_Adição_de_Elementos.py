# Adição de elementos.

# Método append. (adição de elementos)

# Em python chamamos o método escrevendo o nome dele após o nome do objeto.
# Como listas são objetos, logo lista.append(valor).

print('\nAdição de elementos em listas:')
L = []
L.append('a')
print(L)
L.append('b')
print(L)
L.append('c')
print(L)
print(len(L))

#Programa 6.6 - Adição de elementos à lista.

print('\nPrograma que adiciona elementos int dentro da lista.')
L = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        print('\n')
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1

# Outro método para adicionar valores dentro da lista é com adição de listas usando +=

print('\nOutro método para adicionar valores em listas.')
L = []
L = L + [1]
print(L)
L = L + [2]
print(L)
L += [3, 4, 5]
print(L)

# O comando extend. adiciona elementos de uma lista a outra.
# O comando append. se for usado para adicionar uma lista, ele irá adicinar uma 'lista dentro da lista'.
# Já se utilizar o comando extend. , ele irá adicionar os ELEMENTOS da lista para dentro da outra lista.

print('\nUso do comando extend.')
L = ['a']
L.append('b')
print(L)
L.extend(['c'])
print(L)
L.append(['d', 'e'])
print(L)
L.extend(['f', 'g', 'h'])
print(L)

# O método .extend só aceita parâmetros que sejam listas. Sendo assim, é possível adicionar uma lista dentro da outra utilizando o .append e acessar elementos específicos das listas adicionadas.

print('\nAdicionando e acessando uma lista dentro de outra lista:')
L = ['a']
L.append(['b'])
L.append(['c', 'd'])
print(L)
print(len(L))
print(L[1])
print(L[2])
print(len(L[2]))
print(L[2][1])

#Exercício 6.2 - Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

# Opção para adicionar manualmente os números:

l1 = []
l2 = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        print('\n')
        break
    l1.append(n)
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        print('\n')
        break
    l2.append(n)
l3 = l1 + l2
print(l3)

#Exercício 6.3 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

print('\n')
l1 = [1, 3, 6, 8, 9]
l2 = [1, 2, 4, 5, 9]
l3 = []
x = 0
y = 0
while x < len(l1):
    while l1[x] != l2[y]:
        y += 1
        if y == len(l2):
            l3.append(l1[x])
            y = 0
            x += 1
    x += 1
y = 0
x = 0
while x < len(l2):
    while l2[x] != l1[y]:
        y += 1
        if y == len(l1):
            l3.append(l2[x])
            y = 0
            x += 1
    x += 1
print(l3)

#Estava dando erro 'index out of range'. No fim o problema estava com a lista 2, ela não estava em ordem crescente e aparentemente necessita estar em ordem crescente para funcionar.

#Resposta nata grupo do wpp:

print('\n')
l1 = [1, 3, 6, 8, 9]
l2 = [1, 2, 4, 5, 9]
l3 = []
i = j = 0
while i < len(l1) and j < len(l2):
    if l1[i] > l2[j]:
        l3.append(l2[j])
        j += 1
    elif l1[i] == l2[j]:
        i += 1
        j += 1
    elif l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
print(l3)

# O comando .sort() faz com que coloque a lista em ordem crescente.

print('\nExemplo SEM o comando .sort():')
l1 = [1, 3, 6, 8, 9]
l2 = [9, 2, 5, 4, 1]
print(l1)
print(l2)
print('\nExemplo COM o comando .sort():')
l1.sort()
l2.sort()
print(l1)
print(l2)