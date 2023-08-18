class Venda:
    """
    Classe que representa uma venda de produtos para um cliente.

    Atributos:
        produtos (list): Lista de produtos da venda.
        cliente: Cliente associado à venda.
        valor_total (float): Valor total da venda.
    """

    def __init__(self, produtos: list, cliente):
        """
        Inicializa uma instância de Venda.

        :param produtos: Lista de produtos da venda (list).
        :param cliente: Cliente associado à venda.
        """
        # To Do: Implementar para gerar data e hora ao cadastrar a venda
        self.__data_hora = None
        self.__produtos: list = produtos
        self.__cliente = cliente
        self.__valor_total = self.calcular_valor_total()

    def get_data_hora(self):
        """
        Obtém a data e hora da venda.

        :return: Data e hora da venda.
        """
        return self.__data_hora

    def get_produtos(self) -> list:
        """
        Obtém a lista de produtos da venda.

        :return: Lista de produtos da venda (list).
        """
        return self.__produtos

    def set_produtos(self, produtos: list):
        """
        Define a lista de produtos da venda.

        :param produtos: Nova lista de produtos da venda (list).
        """
        self.__produtos = produtos

    def get_cliente(self):
        """
        Obtém o cliente associado à venda.

        :return: Cliente associado à venda.
        """
        return self.__cliente

    def set_cliente(self, cliente):
        """
        Define o cliente associado à venda.

        :param cliente: Novo cliente associado à venda.
        """
        self.__cliente = cliente

    def get_valor_total(self) -> float:
        """
        Obtém o valor total da venda.

        :return: Valor total da venda (float).
        """
        return self.__valor_total

    def calcular_valor_total(self) -> float:
        """
        Calcula e retorna o valor total da venda.

        :return: Valor total da venda (float).
        """
        total = 0
        for produto in self.__produtos:
            total += produto.preco
        return total

    data_hora = property(get_data_hora)
    produtos = property(get_produtos, set_produtos)
    cliente = property(get_cliente, set_cliente)
    valor_total = property(get_valor_total)
