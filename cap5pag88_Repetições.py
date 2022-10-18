#Repetições

pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')
    if questão == 1 and resposta == 'b':
        pontos = pontos + 1
    if questão == 2 and resposta == 'a':
        pontos = pontos + 1
    if questão == 3 and resposta == 'd':
        pontos = pontos + 1
    questão = questão + 1
print (f'O aluno fez {pontos} ponto(s).')

#Exercício 5.10 - Mofifique o programa da questão para que aceite resposta com letras maiúsculas e minúsculas em todas as questões.

pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')
    if questão == 1 and resposta == 'b' or resposta == 'B':
        pontos = pontos + 1
    if questão == 2 and resposta == 'a' or resposta == 'A':
        pontos = pontos + 1
    if questão == 3 and resposta == 'd' or resposta == 'D':
        pontos = pontos + 1
    questão = questão + 1
print (f'O aluno fez {pontos} ponto(s).')

#Acumuladores

#Nesse exemplo podemos ver que 'soma = soma + x' está fazendo a operação da soma acumulada enquanto 'n = n + 1' está fazendo o papel de repetição da operação.

n = 1
soma = 0
while n <= 10:
    x = int(input(f'\nDigite o {n} número: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {soma}.')

x = 1
soma = 0
while x <= 5:
    n = int(input(f'\n{x}n° Digite o número: '))
    soma = soma + n
    x = x + 1
print(f'Média: {soma / 5:.2f}')

#Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses e também o valor total com juros.

x = 1
inicial = int(input('\nQual o valor inicial do depósito? '))
juros = float(input('Qual é a taxa de juros? '))
juros = juros / 100
valor_juros = inicial*juros
valor_mensal = inicial
print('\n')
while x <= 24:
    valor_juros_mensal = valor_mensal * juros
    valor_mensal = valor_mensal + valor_juros_mensal
    print(f'Mês {x}: Valor total: R${valor_mensal:.2f} | Valor rendimento: {(valor_mensal - inicial):.2f}')
    x = x + 1
juros_total =  valor_mensal - inicial
print(f'\nO valor total acumulado é de R${valor_mensal:.2f} e o valor total em juros foi de R${juros_total:.2f}')