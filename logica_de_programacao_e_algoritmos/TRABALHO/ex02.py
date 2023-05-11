print("Bem Vindo a Lanchonete do Gabriel Bonifacio Possomato\n" \
      "*******************cardápio******************* \n" \
      "| Código |         Descrição       | Valor   |\n" \
      "|--------|-------------------------|---------|\n" \
      "| 100    | Cachorro-Quente         |   9,00  |\n" \
      "| 101    | Cachorro-Quente Duplo   |  11,00  |\n" \
      "| 102    | X-Egg                   |  12,00  |\n" \
      "| 103    | X-Salada                |  13,00  |\n" \
      "| 104    | X-Bacon                 |  14,00  |\n" \
      "| 105    | X-Tudo                  |  17,00  |\n" \
      "| 200    | Refrigerante Lata       |   5,00  |\n" \
      "| 201    | Chá Gelado              |   4,00  |")

# Tabela de produtos
tabela_produtos = {
    100: ("Cachorro-Quente", 9.00),
    101: ("Cachorro-Quente Duplo", 11.00),
    102: ("X-Egg", 12.00),
    103: ("X-Salada", 13.00),
    104: ("X-Bacon", 14.00),
    105: ("X-Tudo", 17.00),
    200: ("Refrigerante Lata", 5.00),
    201: ("Chá Gelado", 4.00)
}

total = 0.0

while True:
    # Entrada do código do produto
    codigo = int(input("Digite o código do produto desejado: "))

    # Verificação se o código é válido
    if codigo not in tabela_produtos:
        print("Opção inválida. Tente novamente.")
        continue

    # Adição do valor do produto ao total
    total += tabela_produtos[codigo][1]

    # Impressão do produto selecionado e seu valor
    print(f"{tabela_produtos[codigo][0]} - R$ {tabela_produtos[codigo][1]:.2f}")

    # Pergunta se o cliente quer pedir mais alguma coisa
    while True:
        continuar = input("Deseja pedir mais alguma coisa? (s/n): ").lower()
        if continuar == "s":
            break
        elif continuar == "n":
            # Encerramento da conta e impressão do valor total
            print(f"Total a pagar: R$ {total:.2f}")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            continue