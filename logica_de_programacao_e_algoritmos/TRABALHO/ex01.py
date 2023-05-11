# Exibe uma mensagem de boas-vindas para o usuário
print('Bem Vindo a Loja do Gabriel Bonifacio Possomato')

# Solicita que o usuário insira o valor do produto e armazena o valor na variável "valor1"
valor1 = float(input('Entre com o valor do produto: '))

# Solicita que o usuário insira a quantidade do produto e armazena o valor na variável "valor2"
valor2 = int(input('Entre com o valor da quantidade: '))

# Calcula o valor total do produto multiplicando o valor pela quantidade
total = valor1 * valor2

# Verifica a quantidade do produto e aplica o desconto de acordo com as regras estabelecidas
if valor2 <= 9:
    porcentagem = '(desconto 0%)'
    desconto = total
elif valor2 >= 10 and valor2 <= 99:
    porcentagem = '(desconto 5%)'
    desconto = total * 0.95
elif valor2 >= 100 and valor2 <= 999:
    porcentagem = '(desconto 10%)'
    desconto = total * 0.90
else:
    porcentagem = '(desconto 15%)'
    desconto = total * 0.85

# Exibe o valor total do produto sem desconto
print(f'O valor sem desconto foi: R$ {total:.2f}')

# Exibe o valor do produto com desconto e a porcentagem de desconto aplicada
print(f'O valor com desconto foi: R$ {desconto:.2f} {porcentagem}')
