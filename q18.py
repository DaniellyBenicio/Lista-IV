'''Crie uma função que receba duas listas de números e retorne uma nova lista 
contendo apenas os elementos que estão presentes em ambas as listas.'''

def lista():
    lista1 = []
    lista2 = []
    ambosnumerosnalista = []
    
    qntlista1 = int(input('Informe a quantidade de números para ser adicionado a lista 01: '))
    for i in range(qntlista1):
        n = int(input(f'Digite {i+1}º número: '))
        lista1.append(n)
        
    qntlista2 = int(input('Informe a quantidade de números para ser adicionado a lista 02: '))
    for i in range(qntlista2):
        n = int(input(f'Digite {i+1}º número: '))
        lista2.append(n)

    for num in lista1:
        if num in lista2:
            ambosnumerosnalista.append(num)    
    return ambosnumerosnalista
        
r = lista()
if len(r) == 0:
    print('Não há números em comum nas listas!')
else: 
    print('Os números presentes em ambas as listas são: ', r)

