'''Escreva um programa que leia uma lista de números inteiros e
crie uma lista encadeada simples com esses números em ordem inversa'''

class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None #o ponteiro que vai apontar para o próximo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None
    
    def tam(self):
        return self.tamanho
    
    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.inicio
        self.inicio = novo_item
        self.tamanho +=1
    
    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.inicio is None: #se a lista esta vazia informa a exceção
            raise Exception('A lista está vazia!')
        else:
            self.inicio = self.inicio.proximo
        self.tamanho -=1
        
    def remover_final(self):
        if self.vazia(): #se a lista esta vazia informa a exceção
            raise Exception('A lista está vazia!')
        
        if self.inicio.proximo is None:
            self.inicio = None
        self.tamanho -= 1
        
        atual = self.inicio
        anterior = None
        while atual.proximo is not None:
            anterior = atual
            atual = atual.proximo
        anterior.proximo = None
        self.tamanho -=1
        
    def listar(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        atual = self.inicio
        
        while atual is not None:
            print(atual.dado, end= '\n')
            atual = atual.proximo
        
    def buscar(self, valor):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        atual = self.inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False    
    
def inversa():
    l = ListaEncadeada()
    
    num = int(input('Informe a quantidade de números deseja introduzir na lista:  '))
    for i in range(num):
        n = int(input(f'Informe o {i + 1}º número: '))
        l.inserir_inicio(n)
    l.listar()

inversa()