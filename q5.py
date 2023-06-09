'''Implemente uma fila circular utilizando um vetor e as operações básicas.'''




class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.vetor = []
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def vazia(self):
        return self.tamanho == 0
    
    def tam(self):
        return self.tamanho
    
    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            novo_item.proximo = novo_item
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.proximo = self.inicio
            self.inicio = novo_item
            self.fim.proximo = self.inicio
        self.vetor.append(novo_item)
        self.tamanho += 1
    
    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            novo_item.proximo = novo_item
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.proximo = self.inicio
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.vetor.append(novo_item)
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.vazia():
            raise Exception('A lista está vazia!')
        item_removido = self.inicio
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.fim.proximo = self.inicio
        self.vetor.remove(item_removido)
        self.tamanho -= 1
        
    def remover_final(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        item_removido = self.fim
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            atual = self.inicio
            while atual.proximo != self.fim:
                atual = atual.proximo
            atual.proximo = self.inicio
            self.fim = atual
        self.vetor.remove(item_removido)
        self.tamanho -= 1
        
    def listar(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        atual = self.inicio
        while True:
            print(atual.dado)
            atual = atual.proximo
            if atual == self.inicio:
                break
    
    def buscar(self, valor):
        if self.vazia():
            raise Exception('A lista está vazia!')
        for item in self.vetor:
            if item.dado == valor:
                return True
        return False
    
l = ListaCircular()

l.inserir_inicio(21)
l.inserir_inicio(22)
l.inserir_final(96)
l.inserir_final(15)
print('Números inseridos: ')
l.listar()
print()
print('Tamanho da lista:  ', l.tam())


l.inserir_inicio(2)
l.remover_final()
l.remover_inicio()
print()
l.listar()

print('Tamanho da lista circular: ', l.tam())
