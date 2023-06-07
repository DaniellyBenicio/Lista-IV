'''Escreva uma função que receba uma lista de dicionários, onde cada dicionário representa um aluno 
com as chaves "nome" e "nota". A função deve retornar o nome do aluno com a maior nota.'''

def alunocom_maiornota():
    lista_alunos = []
    
    qntalunos = int(input('Quantos alunos deseja adicionar? '))
    
    for i in range(qntalunos):
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Informe a nota dele: '))
        aluno = {'nome': nome, 'nota': nota}
        lista_alunos.append(aluno)
    
    maiornota = lista_alunos[0]
    
    for aluno in lista_alunos:
        valor = aluno['nota']
        if valor > maiornota['nota']:
            maiornota = aluno
    
    return maiornota['nome'], maiornota['nota']

alunomaiornota = alunocom_maiornota()
print('O aluno com maior nota é: ', alunomaiornota)     

