from arquivos import ler_arquivo

def leiaInt(n):
     valor = input(n)
     if valor.isnumeric():
          return int(valor)
     

def opcoes(*txt):
        for i , c in enumerate(txt):
            print(f'{i+1} - {c}')
        opc = leiaInt(cor('Qual opção: ' , 'ciano'))
        return opc

def titulo(text):
    tamanho = len(text)+10
    print(tamanho*cor('=' , 'roxo'))
    print(text.center(20))
    print(tamanho*cor('=','vermelho'))

def cor(texto, cor):
    cores = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'branco': '\033[37m',
        'reset': '\033[m'
    }

    return f"{cores.get(cor, cores['reset'])}{texto}{cores['reset']}"