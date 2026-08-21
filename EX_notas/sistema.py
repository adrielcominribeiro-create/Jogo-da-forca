from utilidades import *

alunos_geral = []
aluno = {}

while True:
    aluno['nome'] = input('Digite o nome do aluno: ')
    aluno['sexo'] = input('Digite o sexo do aluno: [M/F]')
    nota1 = float(input('Digite a nota do aluno: '))
    nota2 = float(input('Digite a outra nota do aluno: '))

    notafinal = (nota1 + nota2) / 2
    status = verficar_aprovação(notafinal)
    aluno['media'] = notafinal
    aluno['status'] = status


    alunos_geral.append(aluno.copy())
    aluno.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

gerar_relatorio(alunos_geral)