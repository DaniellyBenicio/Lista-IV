



class Item:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
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
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.proximo = self.inicio
            self.inicio.anterior = novo_item
            self.inicio = novo_item
        self.tamanho += 1

    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.anterior = self.fim
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho += 1

    def remover_inicio(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        self.tamanho -= 1

    def remover_final(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        self.tamanho -= 1

    def buscar(self, elemento):
        if self.inicio is None:
            raise Exception("A lista está vazia!")
        atual = self.inicio
        while atual is not None:
            if atual.dado == elemento:
                return True
            atual = atual.proximo
        return False

    def listar(self):
        if self.inicio is None:
            raise Exception("A lista está vazia!")
        atual = self.inicio
        while atual is not None:
            print(atual.dado, end=' \t')
            atual = atual.proximo


l = ListaDuplamenteEncadeada()

l.inserir_inicio(2)
l.inserir_inicio(5)
l.inserir_final(12)
l.inserir_final(20)
l.listar()
print()
l.remover_final()
l.remover_inicio()
l.listar()
