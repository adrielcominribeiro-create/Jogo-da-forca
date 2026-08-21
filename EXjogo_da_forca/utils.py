def escolha_animal(txt):
    from random import choice
    escolher = choice(txt)
    return escolher

def atualizar_tabela(tentativa_usuario , escolha_computador , palavra_escohida):
    if tentativa_usuario in escolha_computador:
        for indice , letra in enumerate(escolha_computador):
            if letra == tentativa_usuario:
                palavra_escohida[indice] = letra

def tentativa_usuario(dados , palavra ):
    if dados not in palavra:
        return True
    else:
        return False

def mostrar_tabela(txt):
    for letra in txt:
        print(letra,end=' ')
    return txt