continuar = 'sim'
operacoes = ['+', '-', '*', '/']

while continuar == 'sim':
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    escolha = input('Escolha a operação [+, -, *, /]: ')

    if escolha == '+':
        operacao = 'soma'
        resultado = num1 + num2
    elif escolha == '-':
        operacao = 'subtração'
        resultado = num1 - num2
    elif escolha == '*':
        operacao = 'multiplicação'
        resultado = num1 * num2
    elif escolha == '/':
        operacao = 'divisão'
        resultado = num1 / num2
    elif escolha != operacoes:
        print('ERRO - DIGITE CORRETAMENTE')
        continue

    print(f'A {operacao} de {num1} com {num2} é {resultado}')

    continuar = input('Deseja continuar? [ sim / não]: ')
    if continuar != 'sim':
        print('encerrando programa...')
