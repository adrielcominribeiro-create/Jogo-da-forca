estoque = {'banana': 22, 'maça': 15, 'manga': 10}

while True:
    try:
        #mostrar estoque
        print(f'ESTOQUE DISPONIVEL')
        for pr , quantidade in estoque.items():
            print(f'{pr} =  {quantidade}')

        #escolha e quantidade do produto
        produto = str(input('Digite o nome do produto: '))

        #veirifca se tem
        if produto in estoque:

            #quantidade desejada
            quantidade = int(input('Digite a quantidade de produto: '))

            #verifica se tem a quantidade
            if quantidade <= estoque[produto]:
                #diminui
                estoque[produto] -= quantidade
            else:
                print('Quantidade insuficiente')
        else:
            print('produto nao disponivel')
    except:
        print('Erro de dados')

    #encerramento seguro
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print('Programa finalizado')
        break
    #resposta de erro a o finalizar
    elif continuar != 'S':
        print('Comando invalido')
