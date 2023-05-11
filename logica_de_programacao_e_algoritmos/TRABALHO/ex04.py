# identificador
print('Bem Vindo ao Controle de Estoque do Gabriel Bonifacio Possomato')

# Inicialização do contador de códigos
codigo = 1

# Lista de peças cadastradas
pecas = []

# Função para cadastrar peça
def cadastrarPeca():
    global codigo
    print(f"\nCódigo da Peça: {codigo:03d}")
    contador = f"{codigo:03d}"
    peca = {}
    peca['codigo'] = codigo
    peca['nome'] = input("Digite o nome da peça: ")
    peca['fabricante'] = input("Digite o fabricante da peça: ")
    peca['valor'] = float(input("Digite o valor da peça: "))
    pecas.append(peca)
    codigo += 1
    print("Peça cadastrada com sucesso!\n")

# Função para consultar peças
def consultarPeca():
    while True:
        print("\nConsultar Peça:")
        print("1 - Consultar Todas as Peças")
        print("2 - Consultar Peças por Código")
        print("3 - Consultar Peças por Fabricante")
        print("4 - Retornar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            print("Todas as Peças:")
            for peca in pecas:
                print(f"Código: {peca['codigo']}\tNome: {peca['nome']}\tFabricante: {peca['fabricante']}\tValor: R${peca['valor']:.2f}")
            print()
        elif opcao == 2:
            codigo = int(input("Digite o código da peça: "))
            for peca in pecas:
                if peca['codigo'] == codigo:
                    print(f"Código: {peca['codigo']}\tNome: {peca['nome']}\tFabricante: {peca['fabricante']}\tValor: R${peca['valor']:.2f}")
                    break
                else:    
                    print("Peça não encontrada.\n")
        elif opcao == 3:
            fabricante = input("Digite o nome do fabricante: ")
            encontrou = False  # variável para verificar se encontrou alguma peça para o fabricante
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    encontrou = True  # atualiza a variável encontrou
                    print(f"Código: {peca['codigo']}\tNome: {peca['nome']}\tFabricante: {peca['fabricante']}\tValor: R${peca['valor']:.2f}")
            if not encontrou:
                print("Não há peças cadastradas para este fabricante.\n")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Função para remover peça
def removerPeca():
    codigo = int(input("Digite o código da peça que deseja remover: "))
    for peca in pecas:
        if peca['codigo'] == codigo:
            pecas.remove(peca)
            print("Peça removida com sucesso!\n")
            break
    else:
        print("Peça não encontrada.\n")

# Loop principal
while True:
    print("\nMenu de Opções:")
    print("1 - Cadastrar Peça")
    print("2 - Consultar Peça")
    print("3 - Remover Peça")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrarPeca()
    elif opcao == 2:
        consultarPeca()
    elif opcao == 3:
        removerPeca()
    elif opcao == 4:
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")

