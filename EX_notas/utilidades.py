def verficar_aprovação(n):
    status =  ''
    if n < 5:
        status  = 'Reprovado'
    if n >= 5 and n < 7 :
        status = 'recuperaçãp'
    if n  >= 7:
        status = 'Aprovado'
    return status

def gerar_relatorio(alunos):
    print('-' * 60)
    print(f'{"NOME":<20} {"SEXO":<10} {"MÉDIA":<10} {"STATUS":<15}')
    print('-' * 60)

    for aluno in alunos:
        print(
            f'{aluno["nome"]:<20} '
            f'{aluno["sexo"]:<10} '
            f'{aluno["media"]:<10.1f} '
            f'{aluno["status"]:<15}'
        )

    print('-' * 60)