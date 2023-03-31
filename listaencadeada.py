class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista_Encadeada:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def lista_vazia(self):
        return self.head == None

    def lista_tamanho(self):
        return self.tamanho

    def obter_valor(self, indice):
        if indice < 1 or indice > self.tamanho:
            print("posicao invalida")
            return None
        aux = self.head
        for i in range(1, indice):
            aux = aux.proximo
        return aux.valor

    def modificar_valor(self, indice, valor):
        if indice < 1 or indice > self.tamanho:
            print("posicao invalida")
            return None
        aux = self.head
        for i in range(1, indice):
            aux = aux.proximo
        aux.valor = valor

    def inserir_elemento(self, indice, valor):
        if indice < 1 or indice > self.tamanho+1:
            print("posicao invalida")
            return None
        no = No(valor)
        if indice == 1:
            no.proximo = self.head
            self.head = no
        else:
            aux = self.head
            for i in range(1, indice-1):
                aux = aux.proximo
            no.proximo = aux.proximo
            aux.proximo = no
        self.tamanho += 1

    def remover_elemento(self, indice):
        if indice < 1 or indice > self.tamanho:
            print("posicao invalida")
            return None
        if indice == 1:
            self.head = self.head.proximo
        else:
            aux = self.head
            for i in range(1, indice-1):
                aux = aux.proximo
            aux.proximo = aux.proximo.proximo
        self.tamanho -= 1

    def imprimir_lista(self):
        aux = self.head
        while aux:
            print(aux.valor)
            aux = aux.proximo

lista = Lista_Encadeada()
print("lista vazia: ")
print(lista.lista_vazia())

lista.inserir_elemento(1, 12)
lista.inserir_elemento(2, 13)
lista.inserir_elemento(3, 14)
lista.inserir_elemento(2, 15)

print("tamanho da lista: ")
print(lista.lista_tamanho()) 

print("valores da lista: ")
lista.imprimir_lista() 

print("modificando valor da lista: ")
lista.modificar_valor(3, 25)

print("valores da lista: ")
lista.imprimir_lista()

print("removendo elemento da lista")
lista.remover_elemento(2)

print("valores da lista: ")
lista.imprimir_lista()
