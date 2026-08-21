import utilidades_prA.uteis as op
'''
variavel (pergunta) que faz a pergunta onde o usuario vai escrever 
variavel (resultado) mostra o final do processo da frase  
'''
pergunta = op.leitor('Escreva uma frase com A: ').lower()
resultado = op.coletorvogais(pergunta)
for i , e in resultado.items():
    print(f'Letra {i} nas posições {e}')