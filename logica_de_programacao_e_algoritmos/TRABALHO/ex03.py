
# identificador
print('Bem Vindo a Companhia de Logística Gabriel Bonifacio Possomato')

# definindo a função dimensoesObjeto que irá receber as dimensões (altura, largura e comprimento)
# do objeto e calcular o volume da caixa para o objeto, retornando o valor em (RS) conforme a Quadro 1
def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            # calculando o volume do objeto em cm³
            volume = altura * largura * comprimento
            print(f"Volume do objeto: {volume} cm³")
            # verificando o valor do volume para determinar o valor do objeto conforme a Quadro 1
            if volume < 1000:
                return 10
            elif volume < 10000:
                return 20
            elif volume < 30000:
                return 30
            elif volume < 100000:
                return 50
            else:
                print("O objeto é muito grande para ser transportado. Tente novamente.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

# definindo a função pesoObjeto que irá receber o peso do objeto e retornar o multiplicador
# conforme o Quadro 2
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            # verificando o valor do peso para determinar o multiplicador conforme o Quadro 2
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                print("O objeto é muito pesado para ser transportado.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

# definindo a função rotaObjeto que irá receber a rota do objeto e retornar o multiplicador
# conforme o Quadro 3
def rotaObjeto():
    while True:
        try:
            rota = input("Selecione a rota:\n" \
                        "BR - De Brasília para Rio de Janeiro\n" \
                        "BS - De Brasília para São Paulo\n" \
                        "RB - De Rio de Janeiro para Brasília\n" \
                        "RS - De Rio de Janeiro para São Paulo\n" \
                        "SR - De São Paulo para Rio de Janeiro\n" \
                        "SB - De São Paulo para Brasília\n" \
                        ">>")
            # verificando a rota para determinar o multiplicador conforme o Quadro 3
            if rota == "RS" or rota == "SR":
                return 1
            elif rota == "BS" or rota == "SB":
                return 1.2
            elif rota == "BR" or rota == "RB":
                return 1.5
            else:
                print("Rota inválida. Tente novamente.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

# obtendo as informações do objeto e da rota
valor_dimensoes = dimensoesObjeto()
valor_peso = pesoObjeto()
valor_rota = rotaObjeto()

# calculando o valor total a ser pago com base na equação fornecida no enunciado
valor_total = valor_dimensoes * valor_peso * valor_rota

# exibindo o valor total a ser pago
print(f"O valor total a ser pago é de R${valor_total:.2f}.")
