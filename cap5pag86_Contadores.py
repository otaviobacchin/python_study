#Contadores

#Contador de 1 até valor desejado:
    
fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    print(x)
    x = x + 1

#Contador de 0 até o valor desejado somente com números pares:
    
fim = int(input('\nDigite o último número a imprimir(somente pares): '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

#Contador de 0 até o número desejado somente com números pares v2:
    
fim = int(input('\nDigite o último número a imprimir (somente pares): '))
x = 0
while x <= fim:
    print(x)
    x = x + 2
    
#Exercício 5.4 - Modifique o programa para imprimir de 1 até o número digitado só com número ímpares.

fim = int(input('\nDigite o último número a imprimir (somente ímpares): '))
x = 1
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1 

#Opção 2:
    
fim = int(input('\nDigite o último número a imprimir (somente ímpares): '))
x = 1
while x <= fim:
    print(x)
    x = x + 2
    
# Exercício 5.5 - Modifique o programa para mostrar somente múltiplos de 3:
    
fim = int(input('\nDigite o último número a imprimir (mútiplos de 3): '))
x = 1
while x <= fim:
    if x % 3 == 0:
        print(x)
    x = x + 1
    
#Código para mostrar múltiplos de tal valor:
#Mútiplos de 2
# x % 2 == 0
#Mútiplos de 3
# x % 3 == 0
#Mútiplos de 4
# x % 4 == 0

# Tabuada de adição:
    
n = int(input('\nTabuada de adição de: '))
x = 1
while x <= 10:
    print(n + x)
    x = x + 1
    
# Exercício 5.6 - Altere o programa para fazer a tabuada de multiplicação:
    
n = int(input('\nTabuada de mútiplicação de: '))
x = 1
while x <= 10:
    print(n * x)
    x = x + 1
    
#Exercício 5.7 - Modifique o programa para que o usuário também diga o início e o fim da tabuada:
    
n = int(input('\nTabuada de: '))
inicio = int(input('Início da tabuada: '))
fim = int(input('Fim da tabuada: '))
while inicio <= fim:
    print(n * inicio)
    inicio = inicio + 1
    
#Exercício 5.8 - Programa para ler 2 números e  faça a multiplicação do primeiro pelo segundo sem utilizar o recurso de multiplicação:

print('\nEscolha 2 valores para multiplicar.')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
nx = n1
vezes = 1
while vezes <= n2:
    nx = n1 + nx
    vezes = vezes + 1
print(nx)

#Exercício 5.9 - Programa para ler 2 números e  faça a divisão inteira do primeiro pelo segundo e também mostre o resto, sem utilizar o recurso de divisão:

print('\nEscolha 2 valores para multiplicar.')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
sobra = n1
inteiro = 1
while sobra >= n2:
    sobra = sobra - n2
    if sobra < n2:
        print(f'A divisão inteira é: {inteiro} e sobra é {sobra}')
    inteiro = inteiro + 1
