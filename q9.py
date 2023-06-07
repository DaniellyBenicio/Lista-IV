'''Um banco precisa armazenar as informações dos clientes em uma lista encadeada simples. 
Cada cliente possui nome, número da conta e saldo. Implemente as operações de inserir, remover e pesquisar
um cliente na lista. A cada operações, mostrar a lista em “formado de tabela”.'''

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
        print('-------------------------------------------------------------')
        print('Nome\t\t\tNúmero_Conta\t\t\tSaldo')
        print('-------------------------------------------------------------')
        atual = self.inicio
        
        while atual is not None:
            nome, num_conta, saldo = atual.dado
            print(f'{nome:10}\t\t{num_conta:10}\t\t{saldo:10}')
            atual = atual.proximo
        
    def buscar(self, valor):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        atual = self.inicio
        while atual is not None:
            if atual.dado[0] == valor:
                return True
            atual = atual.proximo
        return False    

def cliente():
    l = ListaEncadeada()
    while True:
        print('''------Banco do Brasil------
        [1] - Inserir Cliente
        [2] - Remover Cliente
        [3] - Pesquisar Cliente
        [4] - Mostrar lista de Clientes
        [0] - Sair''')
        op = int(input('Informe a opção desejada: '))
        
        
        if op == 0:
            print('Programa encerrado!')
            break
        
        elif op == 1:
            nome = input('Digite o nome do cliente: ')
            num_conta = input('Digite o número da conta: ')
            saldo = float(input('Digite o saldo da conta: '))
            l.inserir_final((nome, num_conta, saldo))
            print('Cliente adicionado com sucesso!')
            
        elif op == 2:
            if l.vazia():
                print('A lista está vazia!')
            else:
                nome = input('Qual cliente deseja remover? ')
                remover = l.buscar(nome)
                if remover:
                    l.remover_inicio()
                    print('Cliente removido com sucesso!')
                else:
                    print('Cliente não encontrado!')
                    
        elif op == 3:
            if l.vazia():
                raise Exception("A lista está vazia!")

            nome = input('Digite o nome do cliente a ser pesquisado: ')
            encontrar = l.buscar(nome)
            
            if encontrar:
                print('O cliente está na lista.')
            else:
                print('O cliente não está na lista.')
                
        elif op == 4:
            l.listar()

cliente()