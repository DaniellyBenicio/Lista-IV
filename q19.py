'''Implemente uma função que receba uma lista de palavras e retorne a palavra mais longa presente na lista.'''

def longa():
    palavras = []

    qntpalavra = int(input('Informe a quantidade de palavas que deseja na lista: '))
    for i in range(qntpalavra):
        palavra = input(f'Informe a {i+1}ª palavra: ')
        palavras.append(palavra)
        
    maislonga = ''
    for palavra in palavras:
        if len(palavra) > len(maislonga):
            maislonga = palavra
    return maislonga

r = longa()
print('Palavra mais longa: ', r)