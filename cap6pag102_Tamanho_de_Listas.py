# Tamanho de listas.

# Podemos usar a função 'len' com listas, o valor retornado é igual ao número de elementos da lista.

print('Função len com listas:')
L = [12, 9, 5]
print(len(L))
V = []
print(len(V))

# A função lenj pode ser utilizada em repetições para controlar o limite dos índices:

#Programa 6.4 - Repetição com tamanho fixo da lista.

print('\nRepetição com tamanho fixo da lista:')
L = [1, 2, 3]
x = 0
while x < 3:
    print(L[x])
    x += 1

#Programa 6.5 - Repetição com tamanho da lista usando len.

print('\nRepetição com tamanho da lista usando len:')
L = [1, 2, 3]
x = 0
while x < len(L):
    print(L[x])
    x += 1

# A vantagem de utilizar a repetição com a função len é que se mesmo se a lista aumentar de tamanho,
# ela irá calcular o mesmo tamanho programado:

print('\nRepetição mostrando até certo elemento da lista:')
L = [1, 2, 3, 4, 5, 6, 7, 8]
x = 0
while x < 5:
    print(L[x])
    x += 1