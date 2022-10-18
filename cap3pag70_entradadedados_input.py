#Input é usado para o programa receber dados ou valores por um dispositivo de entrada de dados como um teclado ou cd.

from ctypes import POINTER


(print('Usamos o comando input para o programa receber dados de um dispositivo externo:'))
nome = input('Digite seu nome: ')
print(f'Você digitou {nome}.')
print(f'Olá {nome}!')

#A função input sempre recebe o dados em formato string, é necessário converter o dado recebido para outro formato caso desejado.

#Nesse exemplo vamos utilizar a função input para dados tipo int ou float:

print('\nCalcule quanto te bônus você receberá:')
anos = int(input('Anos de serviço: '))
valor_por_ano = float(input('Valor por ano: '))
bonus = anos * valor_por_ano
print(f'Bônus de R${bonus:.2f}')