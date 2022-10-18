#Pag.72 - Exercícios

#Exercício 3.7

print('Exercício 3.7: Somar 2 números.')
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
resultado = numero1 + numero2
#Resultado utilizando o comando .format:
print ('A soma dos dois números  utilizando comando .format é: {0}' .format (resultado))
#Também pode ser feito dessa maneira:
print ('A soma dos dois números utilizando virgula é:', resultado)
#Ou também utilizando %:
print('A soma dos dois números utilizando comando porcento é: %d' % resultado)
#Utizando o comando f antes da String, economiza tempo para utilizar o comando .format
print(f'A soma dos dois números utilizando o comando f no início da string é: {resultado}')


#Exercício 3.8

print('\nExercício 3.8: Converter valor de metros em milímetros.')
metros = float(input('Valor em metros: '))
milimetros = metros*1000
print(f'O valor em milímetros é: {milimetros}')

#Exercício 3.9

print('\nExercício 3.9: Inserir valor em dias, horas, minutos, segundos e calcular o total em segundos.')
dias = int(input('Quantidade de dias: '))
horas = int(input('Quantidade de horas: '))
minutos = int(input('Quantidade de minutos: '))
segundos = int(input('Quantidade de segundos: '))
conversao = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f'O valor em segundos é: {conversao}')

#Exercício 3.10

print('\nExercício 3.10: Calcular aumento de salário.')
salario = float(input('Valor do salário:'))
porcentagem_aumento = float(input('Porcentagem do aumento: ')) / 100
valor_aumento = salario*porcentagem_aumento
salario = valor_aumento + salario
print(f'O valor atualizado do salário é: {salario:.2f}')

#Exercício 3.11

print('\nExercício 3.11: Calcule o valor final de um produto com desconto desejado.')
valor_produto = float(input('Valor do produto: '))
porcentagem_desconto = float(input('Desconto: ')) / 100
valor_produto_desconto = float(valor_produto - (valor_produto * porcentagem_desconto))
print(f'O valor com desconto é: {valor_produto_desconto:.2f}')

#Exercício 3.12

print('\nExercício 3.12: Calcule o tempo esperado de uma viagem em base na distância e velocidade média.')
distancia = float(input('Qual a distância? '))
velocidade_media = float(input('Qual a velocidade média? '))
tempo_viagem = int(distancia/velocidade_media) * 60
print(f'O tempo de viagem será de: {tempo_viagem} minutos.')

#Exercício 3.13

print('\nExercício 3.13: Converta C° em °F.')
temperatura = int(input('Temperatura em °C: '))
temperatura_convertida = 9*temperatura/5 + 32
print(f'A temperatura em °F é: {temperatura_convertida}°F')

#Excercício 3.14

print('\nCalcule o valor final do aluguel de um carro pela quantidade de Kms rodados e dias.')
dias_de_uso = int(input('Quantidade de dias: '))
km_rodados = float(input('Quantidade de Kms rodados: '))
valor_final = (dias_de_uso*60) + (km_rodados*0.15)
print(f'O valor total do aluguel do carro é de R${valor_final:.2f}')

#Exercício 3.15

print('Exercício 3.15: Calcule a redução do tempo de vida de um fumante.')
cigarros_por_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = float(input('Há quantos anos você fuma? '))
redução_tempo_de_vida = cigarros_por_dia*(365*anos_fumando) * 0.00694444
print(f'Você perdeu {redução_tempo_de_vida:.0f} dias de vida.')