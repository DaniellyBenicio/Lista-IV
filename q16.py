'''Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.'''

def soma(num):
    lista = []
    soma = 0
    for i in range(num):
        n = int(input(f'Digite {i+1}º número: '))
        lista.append(n)
        soma += n
    return soma

numero = int(input('Informe a quantidade de números deseja adicionar a lista: '))
r = soma(numero)
print('A soma dos números informados: ', r)

'''caso não quisesse informar o parametro num:

def soma():
    lista = []
    soma = 0
    n = int(input('Informe a quantidade de números deseja adicionar a lista: '))
    for i in range(n):
        num = int(input(f'Digite {i+1}º número: '))
        lista.append(n)
        soma += num
    return soma
    
r = soma()
print('A soma dos números informados: ', r)
'''