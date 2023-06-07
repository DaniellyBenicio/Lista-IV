'''Escreva um programa que leia uma lista de números inteiros e crie uma lista encadeada circular
com esses números em ordem crescente. Sua classe lista deve conter métodos/funções para mostrar o 
primeiro e ultimo elemento da lista. '''

class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
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
        if self.tamanho == 1:
            self.fim = self.inicio
            self.fim.proximo = self.inicio
    
    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual != self.fim:
                atual = atual.proximo
            atual.proximo = novo_item
        self.fim = novo_item
        self.fim.proximo = self.inicio
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        else:
            self.inicio = self.inicio.proximo
        self.tamanho -=1
        
    def remover_final(self):
        if self.vazia():
            raise Exception('A lista está vazia!')
        
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        
        atual = self.inicio
        anterior = None
        while atual != self.fim:
            anterior = atual
            atual = atual.proximo
        anterior.proximo = self.inicio
        self.fim = anterior
        self.tamanho -=1
        
    def listar(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        atual = self.inicio
        
        while atual != self.fim:
            print(atual.dado, end= ' ')
            atual = atual.proximo
        print(atual.dado)
        
    def buscar(self, valor):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        atual = self.inicio
        while atual != self.fim:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False 
    
    def primeiro(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        return self.inicio.dado
    
    def ultimo(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        return self.fim.dado

def lista_int():
    l = ListaCircular()
    num = []
    
    qnt = int(input('Quantos números deseja adicionar a lista: '))
    for i in range(qnt):
        n = int(input(f'Digite o {i+1}º número: '))
        num.append(n)
        
    crescente = sorted(num, reverse=False)
    
    print('Números em ordem crescente: ') 
    for numero in crescente:
        l.inserir_final(numero)
    
    l.listar()
    print('Primeiro elemento: ', l.primeiro())
    print('Último elemento: ', l.ultimo())
    
lista_int()