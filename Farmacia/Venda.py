import datetime


class Venda:
    """
    Classe que representa uma venda de produtos para um cliente.

    Atributos:
        produtos (list): Lista de produtos da venda.
        cliente: Cliente associado à venda.
        valor_total (float): Valor total da venda.
    """

    vendas = []

    def __init__(self, produtos: list, cliente):
        """
        Inicializa uma instância de Venda.

        :param produtos: Lista de produtos da venda (list).
        :param cliente: Cliente associado à venda.
        """

        self.__data_hora = datetime.datetime.now()
        self.__produtos: list = produtos
        self.__cliente = cliente
        (
            self.__valor_total,
            self.__houve_desconto,
        ) = self.__calcular_valor_total()
        self.__salvar_venda(self)

    @classmethod
    def __salvar_venda(cls, venda: "Venda") -> None:
        """
        Adiciona um venda à lista de vendas executadas.

        :param venda: Instância de Venda a ser cadastrada.
        """
        cls.vendas.append(venda)

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

    def get_cliente(self):
        """
        Obtém o cliente associado à venda.

        :return: Cliente associado à venda.
        """
        return self.__cliente

    def get_valor_total(self) -> float:
        """
        Obtém o valor total da venda.

        :return: Valor total da venda (float).
        """
        return self.__valor_total

    def get_houve_desconto(self) -> bool:
        """
        Obetém o indicador de desconto para a venda.

        :return: Valor total da venda (float).
        """
        return self.__houve_desconto

    def get_desconto(self) -> float:
        return self.__desconto

    def __calcular_valor_total(self) -> float:
        """
        Calcula e retorna o valor total da venda.

        :return: Valor total da venda (float).
        """

        valor_total = sum(produto.preco for produto in self.__produtos)
        desconto = self.calcular_desconto(valor_total)
        return (valor_total - desconto, desconto > 0)

    def calcular_desconto(self, valor_total):
        desconto_idoso = 0
        desconto_valor = 0

        if self.__cliente.valida_se_idoso():
            desconto_idoso = 0.2
        if valor_total > 150.0:
            desconto_valor = 0.1
        if max(desconto_idoso, desconto_valor) > 0:
            self.__desconto = max(desconto_idoso, desconto_valor)
        return max(desconto_idoso, desconto_valor)

    @classmethod
    def gerar_relatorio_vendas(cls):
        """
        Gera um relatório de vendas contendo as estatísticas de
            um ciclo de venda:
        total de vendas (int),
        total de receita (float),
        produto mais vendido (str),
        total de clientes atendidos (int),
        total de vendas de quimioterápicos(int),
        total de venda de fitoterápicos (int),

        :return: Todos as informações geradas (tuple)
        """
        total_vendas = len(cls.vendas)
        total_receita = sum(venda.valor_total for venda in cls.vendas)

        produto_mais_vendido = None
        max_qtd_vendida = 0
        produto_qtd_vendida = {}
        for venda in cls.vendas:
            for produto in venda.produtos:
                nome_produto = produto.nome
                if nome_produto in produto_qtd_vendida:
                    produto_qtd_vendida[nome_produto] += 1
                else:
                    produto_qtd_vendida[nome_produto] = 1
                if produto_qtd_vendida[nome_produto] > max_qtd_vendida:
                    max_qtd_vendida = produto_qtd_vendida[nome_produto]
                    produto_mais_vendido = nome_produto

        clientes_unicos = set(venda.cliente.nome for venda in cls.vendas)
        total_clientes = len(clientes_unicos)

        total_vendas_quimioterapico = 0
        total_vendas_fitoterapico = 0
        for venda in cls.vendas:
            for produto in venda.produtos:
                if (
                    str(type(produto))
                    == "<class 'Farmacia.Medicamento.MedicamentoFitoterapico'>"
                ):
                    total_vendas_fitoterapico += 1
                elif (
                    str(type(produto))
                    == "<class 'Farmacia.Medicamento.MedicamentoQuimioterapico'>"
                ):
                    total_vendas_quimioterapico += 1

        return (
            total_vendas,
            total_receita,
            produto_mais_vendido,
            total_clientes,
            total_vendas_quimioterapico,
            total_vendas_fitoterapico,
        )

    data_hora = property(get_data_hora)
    produtos = property(get_produtos)
    cliente = property(get_cliente)
    valor_total = property(get_valor_total)
    houve_desconto = property(get_houve_desconto)
    desconto = property(get_desconto)
