'''Escreva um programa que leia uma sequência de números inteiros e insira-os em uma fila até que um número negativo 
seja digitado. Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.'''

class Item:
    def __init__(self, valor):
        self.valor = valor #armazena o valor do elemento
        self.proximo = None #armazena o valor do proximo elemento, que no caso é vazio

class Fila:
    def __init__(self):
        self.inicio = None #pois o primeiro elemento é None, nao existe
        self.fim = None #pois o ultimo elemento tambem é None, nao existe ainda.
        self.tamanho = 0 #como nao tem nada adicionado ainda, o tamanho é 0.
    
    def vazia(self):
        return self.inicio is None #retorna dizendo o que o inicio é None
    
    def tam(self):
        return self.tamanho #retorna qual o tamanho daquela fila.
    
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item #proximo do valor atual no final da fila. pra sempre apontar para o ultimo da fila
            self.fim = novo_item #ultimo elemento da fila
        self.tamanho += 1 
        
    def desenfileirar(self):
        if self.vazia():
            raise IndexError('A fila está vazia!')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -=1
        return valor
        
def sequencia():
    f = Fila()

    while True:
        num = int(input('Informe o número para adicionar a fila: '))
        if num < 0:
            break
        f.enfileirar(num)
    print('Os números foram adicionados a fila!\n')
        
    print('Ordem que os elementos foram inseridos: ')
    while not f.vazia():
        removidos = f.desenfileirar()
        print(removidos)

sequencia()    