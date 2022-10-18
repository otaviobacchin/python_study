#Exercício 4.1: Lê dois valores e diz qual é o maior.

valor1 = float(input('Valor 1: '))
valor2 = float(input('Valor 2: '))
if valor1 > valor2:
    print('O valor 1 é maior que o valor 2.')
if valor1 < valor2:
    print('O valor 2 é maior que o valor 1.')
if valor1 == valor2:
    print('O dois valores são iguais.')

#Exercício 4.2: Programa para ler velocidade de um carro e ver se uma muta é aplicável ou não.

velocidade = float(input('Qual a velocidade em que o carro estava? '))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print(f'Você estava acima da valocidade limite. Sua multa é de R${multa:.2f}.')
if velocidade <= 80:
    print('Você estava dentro do limite de velocidade permitido.')

#Programa 4.3 - Cálculo do Imposto de Renda

salario = float(input('Digite o salário para cálculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000)* 0.20)
print(f'Salário: R${salario:6.2f} Imposto a pagar: R${imposto:.2f}')
