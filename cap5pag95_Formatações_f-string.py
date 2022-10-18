#Formatações com f-strings:

# É possível formatar f-strings especificando o número de caracteres após o nome da variável e dois pontos. Ex:

print('Exemplo de formatação de n° de caracteres f-strings:')
preço = 5.20
print(f'Preço: R${preço:5.2f}')
print(f'Preço: R${preço:10.2f}')
print(f'Preço: R${preço:.2f}')

# Você também pode usar >, < e ^ para alinhar os valores à esquerda, à direita ou ao centro:

print('\nExemplo de alinhamento de f-strings:')
print(f'Preço: R${preço:>10.2f}.')
print(f'Preço: R${preço:<10.2f}.')
print(f'Preço: R${preço:^10.2f}.')

# Também é possível específicar qual caractere deve ser utilizado para preencher os espaços em branco:

print('\nExemplo de preenchimento de espaços em branco f-strings:')
print(f'Preço: R${preço:.^10.2f}.')
print(f'Preço: R${preço:x^10.2f}.')
print(f'Preço: R${preço:_^10.2f}.')

# Utilizando o f-string é possível também fazer funções.

print('\nExemplo de função com f-strings:')
x = 5.1
print(f'\nInteiro: {int(x)}')

# O comando \n faz com que o print quebre uma linha.

valor = 5.50
dia = 'segunda-feira'
diafinal = 'quarta-feira'
print (f'\nO preço do produto é R${valor:.2f}.\nA promoção começa na {dia} e vai até {diafinal}.')