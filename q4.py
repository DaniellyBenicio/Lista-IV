'''Escreva um programa que leia uma frase do usuário e verifique se ela é um palíndromo 
(ou seja, pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda).
Utilize uma fila para armazenar os caracteres da frase.'''

class Item:
    def __init__(self, valor):
        self.valor  = valor
        self.proximo = None
    
class Fila:
    def __init__ (self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def vazia(self):
        return self.inicio is None
    
    def tam(self):
        return self.tamanho
    
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho +=1
    
    def desenfileirar(self):
        if self.vazia():
            raise IndexError("A fila está vazia!")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -=1
        return valor
    
def verificar_palindromo():
    f = Fila()
    
    frase = input('Informe uma frase: ')
    
    for c in frase:
        f.enfileirar(c)
    
    frase_invertida = ''
    
    while not f.vazia():
        caracter = f.desenfileirar()
        frase_invertida = caracter + frase_invertida
    #print('Frase invertida:', frase_invertida)
    return frase_invertida == frase

r = verificar_palindromo()
if r:
    print('A frase/palavra informada é um palíndromo!')
else:
    print('A frase/palavra NÃO é um palíndromo!')

