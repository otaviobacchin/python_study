n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
while n1 > n2:
    n2 += n2
breakpoint()

#Repetições Aninhadas

#Exemplo de while dentro de while:

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{tabuada} x {numero} = {tabuada * numero}')
        numero += 1
    tabuada += 1

#Exemplo sem utilizar while dentro de while:

tabuada = 1
numero = 1
while tabuada <= 10:
    print(f'{tabuada} x {numero} = {tabuada * numero}')
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1

#Exercício 5.21 - Reescreva o prgorama 5.1 e de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.

valor = int(input('\nDigite o valor a pagar: '))
cedula = 100
a_pagar = valor
while a_pagar > 0:
    totcedulas = 0
    while cedula <= a_pagar:
        a_pagar -= cedula
        totcedulas += 1
    print(f'{totcedulas} unidades de R${cedula}')
    if cedula == 100:
        cedula = 50
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 5
    elif cedula == 5:
        cedula = 1

#Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

print('\nSelecione qual operação desejada, seja ela: Soma (+), Subtração (-), Multiplicação (*) e Divisão (/). Ou digite "sair" para sair.')
while True:
    operacao = input('\nSelecione a operação: ')
    if operacao == "sair":
        break
    numero = int(input('Qual o número desejado para a tabuada? '))
    tabuada = 1
    if operacao == '+':
        while tabuada <= 10:
            print(f'{tabuada} + {numero} = {tabuada + numero}')
            tabuada += 1
    if operacao == '-':
        while tabuada <= 10:
            print(f'{numero} - {tabuada} = {numero - tabuada}')
            tabuada += 1
    if operacao == '*':
        while tabuada <= 10:
            print(f'{tabuada} * {numero} = {tabuada * numero}')
            tabuada += 1
    if operacao == '/':
        while tabuada <= 10:
            print(f'{numero} / {tabuada} = {numero / tabuada}')
            tabuada += 1

#Exercício 5.23 - Escreva um programa que leia um número e verifique se é ou não um número primo.

numero = int(input('\nDigite o número para descobrir se é primo ou não: '))
divisor = 2
resto = numero % divisor
if resto == 0:
    print('Esse número não é um número primo.')
else:
    divisor = 3
    resto = numero % divisor
    while divisor != numero:
        resto = numero % divisor
        divisor += 2
        if resto == 0:
            print('Esse número não é primo.')
            break
        else:
            print('Esse número é primo.')
            break

#Exercício 5.24 - Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

n = int(input('\nDigite a quantidade de números primos que deseja visualizar: '))
contador = 3
numero = 4
if n >= 1:
    print(2)
if n >= 2:
    print(3)
divisor = 3
while contador <= n:
    resto = numero % divisor
    divisor += 2
    numero += 1
    if resto != 0:
        print(numero)
        contador += 1
        numero += 1

#Exercício 5.25 - Utilize um programa que calcule a raiz quadrada de um numero n. Utilize o método de Newton para obter o número aproximado.

#NÃO CONSEGUI RESOLVER!!!!!

n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")

#Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre 2 numeros. Utilize somente soma e subtração.

n1 = int(input('Valor: '))
n2 = int(input('Dividido por:  '))
divisor = n2
contador = 1
while n1 > n2:
        n2 += divisor
        contador += 1
if n2 > n1:
    n2 -= divisor
    contador -= 1
sobra = n1 - n2
resultado = contador
print(f'O resultado da divisão é {resultado} e a sobra é {sobra}')

#Exercício 5.27 - Programa para descobrir se um número é Palíndromo, ou seja, que o valor é o mesmo ao contrário dele.

numero = str(input('\nDigite o número para saber se ele é palíndromo: '))
if numero == numero[::-1]:
    print('O número é palíndromo.')
else:
    print('O número não é palíndromo.')