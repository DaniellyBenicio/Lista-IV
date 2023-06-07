'''Implemente uma fila simples e as operações básicas; inserir, remover e mostrar o elemento da frente.'''
#só é possível inserir um novo elemento no final da fila e só é possível remover um elemento do início.
class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
  
    def adicionar(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho += 1
	
    def remover(self):
        if self.vazia():
            raise IndexError("A fila está vazia.")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor

    def vazia(self):
        return self.inicio is None
        
    def tam_fila(self):
        return self.tamanho

def operacoes():
    f = Fila()
       
    num = int(input('Quantos números deseja adicionar a fila: '))
    for i in range(num):
        n = int(input(f'Informe o {i+1}º número: '))
        f.adicionar(n)
    print('Números adicionados a fila!')
    print('Tamanho da fila é: ', f.tam_fila())
    
    while not f.vazia():
        n = f.remover()
        print('Número removido: ', n)
        print('Tamanho da fila: ', f.tam_fila())
    
    
operacoes()
