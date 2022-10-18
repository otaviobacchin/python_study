#Anotações:

# Comando "len" diz quantos caracteres existem dentro da String.

# [ ] Pode ser usado para selecionar um caractere dentro de uma String.

print('Anotações 3.4')
a = '123acb'
print(len(a))
print(a[0])
print(a[2])
print(a[5])

# Concatenação: comando para juntar ou repetir strings.

print('\nConcatenação Exemplos:')
s = "abc"
print(s + 'd')
print(s + 3*'d')
print('x' + 5*'_' + 'x')
print(s + '4x = ' + s*4)

#Obs: a concatenação só pode ser usado com STRINGS.

#Adicionar uma variável no meio de uma String:

print('\nAdicionar uma variável dentro de uma String:')
b = 27
print('Otávio tem %d anos de idade.' %b)
    
# Os marcadores para cada tipo são: %d (números inteiros), %s (strings) e %f (números decimais).

# Comandos para espaçamento e tamanho do número.

print('\nEspaçamento e Tamanho de uma variável')
idade = 22
print('Exemplo 1: %d' % idade)
print('Exemplo 2: %03d' % idade)
print('Exemplo 3: %3d' % idade)
print('Exemplo 4: %-3d' % idade)

# No caso de variáveis do tipo float (decimais), podemos escolher também quantas casas decimais queremos que o programa utilize.

print('\nFormatação de variável tipo Float:')
valor = 5
print('Exemplo 1: %5f' % valor)
print('Exemplo 2: %5.2f' % valor)
print('Exemplo 3: %10.5f' % valor)
print('Exemplo 4: R$%.2f' % valor)

#Exemplo com diversos valores em diferentes formatações dentro de uma String:

print('\nVárias formatações de variáveis int e float dentro de uma String:')
nome = 'João'
idade = 22
grana = 51.34
print('Exemplo 1:')
print('%s tem %d anos e tem R$%.2f no bolso.' % (nome, idade, grana))
print('Exemplo 2:')
print('%12s tem %3d anos e tem R$%5.2f no bolso.' % (nome, idade, grana))
print('Exemplo 3:')
print('%-12s tem %03d anos e tem R$%f no bolso.' % (nome, idade, grana))

#Usamos %.2f para usar formatação de float com apenas DUAS casas decimais (ex: 53.4456143 = %.2f = 53.44)

#Outra forma de adicionar variáveis em uma String é pelo comando .format

print('\nFormatações de int e float em String utilizando o comando .format:')
print('Exemplo 1:')
print('{0} tem {1} anos e tem R${2} no bolso.' .format(nome, idade, grana))
print('Exemplo 2:')
print('{:} tem {:} anos e tem R${:} no bolso.' .format(nome, idade, grana))
print('Exemplo 3:')
print('{:12} tem {:6} anos e tem R${:5.2f} no bolso.' .format(nome, idade, grana))
print('Exemplo 4:')
print('{:<12} tem {:<6} anos e tem R${:5.2f} no bolso.' .format(nome, idade, grana))

#Uma forma mais moderna de se criar string é através do f-strings com o comando f antes de criar uma string.

print('\nFormatações de int e float em f-strings')
print('Exemplo 1:')
print(f'{nome} tem {idade} anos e tem R${grana} no bolso.')
print('Exemplo 2:')
print(f'{nome:12} tem {idade:<6} anos e tem R${grana:5.2f} no bolso.')
print('Exemplo 3:')
print(f'{nome:<12s} tem {idade:03} anos e tem R${grana:5.2f} no bolso.')

#Fatiamento de Strings

print('\nFatiamento de String:')
q = 'abcdefgh'
print('Exemplo 1:')
print(q[1:3])
print('Exemplo 2:')
print(q[5:7])
print('Exemplo 3:')
print(q[2:6])

#Também é possível omitir o número da esquerda ou direita para assim selecionar toda a extensão da variável string.

print('\nOutro modelo de seleção de Fatiamento de String:')
print('Exemplo 1:')
print(q[:3])
print('Exemplo 2:')
print(q[3:])
print('Exemplo 3:')
print(q[:])
print('Exemplo 4:')
print(q[-1:])
print('Exemplo 5:')
print(q[-5:7])
print('Exemplo 6:')
print(q[-4:-2])

