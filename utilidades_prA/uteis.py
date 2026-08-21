def leitor(txt):
    """
    Verifica a frase se ela não tem número,
    verifica se digitaram ou tem vogal na frase
    ela é analisada pela variavel (msg) que é a escrita do usuario
    """
    while True:
        msg = str(input(txt))
        if msg.isnumeric():
            print('não pode número')
        elif not msg or 'a' not in msg:
            print('não tem frase, ou não tem A na frase')
        else:
            return msg

def coletorvogais(msg):
    '''
    Coleta as vogais da frase selecionada pela função leitor
    variavel coletor pega as posições de cada vogal da frase
    '''
    vogais = 'aeiou'
    coletor = {
        'a':[],
        'e':[],
        'i':[],
        'o':[],
        'u':[]
    }
    for i , c in enumerate(msg):
        if c in vogais:
            coletor[c].append(i)

    return coletor
