import utils as u

lista_animais = ['vaca','zebra','leao','gato',
                 'cachorro','coelho','javali',
                 'girafa','passaro','peixe','pantera'
                 ]

pontuacao = 10
#função de escolher aleatoriamente
escolha_computador = u.escolha_animal(lista_animais)
palavra_escohida = ['_'] * len(escolha_computador)
letras_tentadas = set()
print(f'JOGO DA FORCA')

while True:
    #entrada de dados do usuario
    u.mostrar_tabela(palavra_escohida)
    print(f'\n{pontuacao} chances restantes , OBS: se acertar não perde pontuação')
    letra = (str(input('\nTente adivinhar a letra do animal que pensei: ')))

    #mostra a tabela da palavra mostrando as lacunas e a posição da palavra certa
    mostrar = u.atualizar_tabela(letra,escolha_computador,palavra_escohida)

    # mostra o resultado que o usuario faz , se for errado ou certo
    usuario = u.tentativa_usuario(letra,escolha_computador)
    if usuario:
        pontuacao -=1
        print('Palavra ou letra invalida')
    else:
        print('adicionado com sucesso')

    #verifica letra repetida
    if letra in letras_tentadas:
        print(f'Você ja digitou essa letra')
        continue
    letras_tentadas.add(letra)
    print(letras_tentadas)
    #se o usuario acertar
    if letra == escolha_computador:
        print('Você acertou! PARABENS')
        break

    # se o usuario perder
    if pontuacao == 0:
        print('Fim de jogo! Tente novamente')
        break