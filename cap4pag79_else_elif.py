#Utilização do else.

#Exercício 4.5 - Execute o programa 4.4 e verifique se os resultados foram os mesmos do Programa 4.2.

idade = int(input('Digite a idade do seu carro: '))
if idade <= 3:
    print('Seu carro é novo.')
else:
    print("Seu carro é velho.")

#Exercício 4.2: Programa para ler velocidade de um carro e ver se uma muta é aplicável ou não.

velocidade = float(input('Qual a velocidade em que o carro estava? '))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print(f'Você estava acima da valocidade limite. Sua multa é de R${multa:.2f}.')
else:
    print('Você estava dentro do limite de velocidade permitido.')


#Exercício 4.6: Calcule o preço da passagem cobrando R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))
preço_km = 0.5
if distancia <= 200:
    custo_viagem = distancia * preço_km
    print(f'O valor da passagem é de R${custo_viagem:.2f}')
else:
    preço_km = 0.45
    custo_viagem = distancia * preço_km
    print(f'O valor da passagem é de R${custo_viagem:.2f}')

#Programa 4.5 - Conta de telefone com três faixas de preço.

minutos = int(input('Quantos minutos você utilizou este mês? '))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print(f'Você vai pagar este mês: R${minutos*preço:6.2f}')

#Programa 4.6 - Categoria x Preço:

categoria = int(input('Digite a categoria do Produto: '))
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print('Categoria inválida , digite um valor de 1 a 5!')
                    preço = 0
print(f'O preço do produto é: R${preço:6.2f}')

#Utilizacação do elif:

#Programa 4.7 - Categoria x Preço, usando elif:

categoria = int(input('Digite a categoria do Produto: '))
if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    print('Valor inválido, digite uma catergoria de 1 a 5!')
    preço = 0
print(f'O valor do produto é R${preço:6.2f}')

#Exercício 4.8 - Escreva um programa que leia dois números e pergunte qual opreção você deseja realizar (+ - * /):

numero1 = float(input('Qual é o primeiro valor? '))
numero2 = float(input('Qual é o segundo valor? '))
resultado = 0
operaçao = (input('Digite qual operação deseja realizar sendo elas soma (+), subtração (-), divisão (/) ou multiplicação (*): ' ))
if operaçao == '+':
    resultado = numero1 + numero2
elif operaçao == '-':
    resultado = numero1 - numero2
elif operaçao == '/':
    resultado = numero1 / numero2
elif operaçao == '*':
    resultado = numero1 * numero2
print(f'O resultado da operação é: {resultado}')

#Exercício 4.9 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa, sendo que o valor da prestação não pode ser superior a 30% do salário.

valordacasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos deseja parcelar? '))
meses = anos*12
prestações = valordacasa/meses
condição = 0.3*salario
if condição >= prestações:
    print('O seu empréstimo foi aprovado!')
else:
    print('O seu empréstimo foi reprovado!')

#Exercício 4.10 - Escreva um programa para calcular o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação.

energia = float(input('Qual a quantidade de energia consumida? '))
tipo_instalação = str(input('Qual o tipo de instalação sendo Residencial (r), Comercial (c) e Industrial (i): '))
valor_conta = 0
if tipo_instalação == 'r':
    if energia <= 500:
        valor_conta = energia*0.40
    else:
        valor_conta = energia*0.65
elif tipo_instalação == 'c':
    if energia <= 1000:
        valor_conta = energia*0.55
    else:
        valor_conta = energia*0.60
elif tipo_instalação == 'i':
    if energia <= 5000:
        valor_conta = energia*0.55
    else:
        valor_conta = energia*0.60
print(f'O valor total para pagamento é de R${valor_conta:6.2f}')
