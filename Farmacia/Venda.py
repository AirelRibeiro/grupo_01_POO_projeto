class Venda:
    def __init__(self, produtos, cliente):
        # To Do Implementar para gerar data e hora ao cadastrar a venda
        self.__data_hora = None
        self.__produtos: list = produtos
        self.__cliente = cliente
        self.__valor_total = self.calcular_valor_total()

    def get_data_hora(self):
        return self.__data_hora

    def get_produtos(self):
        return self.__produtos

    def set_produtos(self, produtos: list):
        self.__produtos = produtos

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_valor_total(self):
        return self.__valor_total

    def calcular_valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    data_hora = property(get_data_hora)
    produtos = property(get_produtos, set_produtos)
    cliente = property(get_cliente, set_cliente)
    valor_total = property(get_valor_total)
