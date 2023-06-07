'''Implemente uma função que receba uma lista de strings e retorne uma 
nova lista contendo apenas as strings que possuem mais de 5 caracteres.'''

def lista(texto):
    listastring = []
    maior5 = []
    
    for i in range(texto):
        palavra = input(f'Informe a {i + 1}ª palavra: ')
        listastring.append(palavra)
            
        if len(palavra) > 5:
            maior5.append(palavra)
    return maior5

palavras = int(input('Informe a quantidade de palavras deseja adicionar a lista: '))
r = lista(palavras)
print(r)

