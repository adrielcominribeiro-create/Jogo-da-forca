from menu.interface import *
import arquivos as ar
arquivo = 'arquivo.txt'

#Manda mensagem quando a função verificar_arquivo rodar 
var = ar.verificar_arquivo(arquivo)
if var:
     print(f'Arquivo {arquivo} existe')
else:
     print(f'arquivo {arquivo} não existe')
     ar.criar_arquivo(arquivo)


while True:
        titulo('CADASTRO DE PESSOAS')
        menu = opcoes(cor('Cadastrar nova pessoa','verde'),cor('Ver pessoas cadastradas','amarelo'), cor('Sair do sistema' ,'azul'))
        if menu == 1:
            titulo(f'{'OPÇÃO 1'}')
            ar.adicionar_arquivo(arquivo)

        elif menu == 2:
            titulo('OPÇÃO 2')
            titulo(f'{'nome'.upper( ):<30} {'idade'.upper():>3}')
            ar.ler_arquivo(arquivo)

        elif menu == 3:
            titulo('OPÇÃO 3')
            print('Saindo do sistema...')
            break
        else:
            print('Digite uma alternativa válida')

