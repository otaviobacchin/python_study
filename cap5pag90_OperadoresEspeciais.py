#Operadores especiais

#Existem operadores especiais para podermos simplificar a escrita ainda mais, como por exemplo as operações de (x = x + 1) ou (y = y - 1) podemos representar também por += ou -=

# (x += 1) é equivalente a (x = x + 1)
# (x -= 1) é equivalente a (x = x - 1)
# (x *= 1) é equivalente a (x = x * 1)
# (x /= 1) é equivalente a (x = x / 1)
# (x **= 1) é equivalente a (x = x ** 1)
# (x //= 1) é equivalente a (x = x // 1)

x = 1
x = x + 1
print(x)

x = 1
x += 1
print(x)



#Interrompendo a repetição (break)

s = 0
while True:
    v = int(input('Difite um número a somar ou 0 para sair:'))
    if v == 0:
        break
    s += v
print(s)


#Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0. No final de cada execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

s = 0
c = 1
while True:
    v = int(input('\nDigite um número a somar ou 0 para sair:'))
    if v == 0:
        break
    s += v
    c += 1
c = c - 1
media = s / c
print(f'\nA quantidade de números digitados: {c} soma dos valores é igual a {s} e a média aritmética é {media}.')

#Exercício 5.15 - Escreva um programa para controlar uma máquina registradora. Você deve solicitar o código do produto e a quantidade comprada. Utilize a tabela de códigos (pag92), o programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar o erro "Código inválido".

valor = 0
while True:
    codigo = int(input('Digite o código do produto: '))
    if codigo == 1:
        valor += 0.5
    elif codigo == 2:
        valor += 1
    elif codigo == 3:
        valor += 4
    elif codigo == 5:
        valor += 7
    elif codigo == 9:
        valor += 8
    elif codigo == 0:
        break
    else:
        print('Código inválido')
print(f'\nO total da compra é de R${valor:.2f}')

#Programa 5.1 - Contagem de Cédulas

valor = int(input('Digite o valor a pagar: '))
quantidade = 0
cedula = 50
a_pagar = valor
while True:
    if cedula <= a_pagar:
        a_pagar -= cedula
        quantidade += 1
    else:
        print(f'{quantidade} cédula(s) de R${cedula}')
        if a_pagar == 0:
            break
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        quantidade = 0

#Excercício 5.18 - Modifique o programa para trabalhar também com notas de R$100.00

valor = int(input('Digite o valor a pagar: '))
cedula = 100
quantidade = 0
a_pagar = valor
while True:
    if cedula <= a_pagar:
        a_pagar -= cedula
        quantidade += 1
    else:
        print(f'{quantidade} cédula(s) de R${cedula}')
        if a_pagar == 0:
            break
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
        quantidade = 0


#Exercício 5.19 - Modifique o programa para corrigir o erro de números decimais.

valor = float(input('Digite o valor a pagar: '))
cedula = 100.00
a_pagar = valor
quantidade = 0
while True:
    if cedula <= a_pagar:
        a_pagar -= cedula
        quantidade += 1
    else:
        print(f'{quantidade} unidade(s) de R${cedula}')
        if a_pagar == 0:
            break
        if cedula == 100.00:
            cedula = 50.00
        elif cedula == 50.00:
            cedula = 20.00
        elif cedula == 20.00:
            cedula = 10.00
        elif cedula == 10.00:
            cedula = 5.00
        elif cedula == 5.00:
            cedula = 1.00
        elif cedula == 1.00:
            cedula = 0.50
        elif cedula == 0.50:
            cedula = 0.25
        elif cedula == 0.25:
            cedula = 0.10
        elif cedula == 0.10:
            cedula = 0.05
        elif cedula == 0.05:
            cedula = 0.01
        elif cedula == 0.01:
            cedula = 0
        quantidade = 0

#Exercício 5.20 - Se digitar 0.001 o programa irá falhar, resolva este problema.

valor = float(input('Digite o valor a pagar: '))
while valor < 0.1:
    print('Porfavor digite somente números decimais de 2 casas (Ex: 0.40, 23.59, etc).')
    valor = float(input('Digite o valor a pagar: '))
cedula = 100
quantidade = 0
a_pagar = valor
while True:
    if cedula <= a_pagar:
        a_pagar -= cedula
        quantidade += 1
    else:
        print(f'{quantidade} unidade(s) de R${cedula}')
        if a_pagar == 0:
            break
        if cedula == 100.00:
            cedula = 50.00
        elif cedula == 50.00:
            cedula = 20.00
        elif cedula == 20.00:
            cedula = 10.00
        elif cedula == 10.00:
            cedula = 5.00
        elif cedula == 5.00:
            cedula = 1.00
        elif cedula == 1.00:
            cedula = 0.50
        elif cedula == 0.50:
            cedula = 0.25
        elif cedula == 0.25:
            cedula = 0.10
        elif cedula == 0.10:
            cedula = 0.05
        elif cedula == 0.05:
            cedula = 0.01
        elif cedula == 0.01:
            cedula = 0
        quantidade = 0