#Exercício 4.3: Insira 3 valores e mostre o valor maior e o valor menor.

print('Insira 3 valores números distintos:')
valor1 = float(input('Valor 1: '))
valor2 = float(input('Valor 2: '))
valor3 = float(input('Valor 3: '))
valormaior = 0
valormenor = 0
if valor1 > valor2 and valor1 > valor3:
    valormaior = valor1
if valor2 > valor1 and valor2 > valor3:
    valormaior = valor2
if valor3 > valor1 and valor3 > valor2:
    valormaior = valor3
if valor1 < valor2 and valor1 < valor3:
    valormenor = valor1
if valor2 < valor1 and valor2 < valor3:
    valormenor = valor2
if valor3 < valor1 and valor3 < valor2:
    valormenor = valor3
else:
    print('Uma ou mais variável tem o mesmo valor.')
print('O valor maior é {0} e o valor menor é {1}.' .format (valormaior, valormenor))

#Exercício 4.4: Calcule o salário e o aumento de salário. Para salários de R$1.250,00 será de 10% e inferiores a esse valor, de 15%.

print('Calculo de aumento do salário:')
salario = float(input('Qual valor do salário: '))
aumento = 0.15
if salario > 1250.00:
    aumento = 0.1
valor_do_aumento = salario*aumento
print(f'O valor do aumento é de R${valor_do_aumento:.2f}')
