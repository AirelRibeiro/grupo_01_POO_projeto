class Controller:
    def __init__(
        self, cliente, laboratorio, quimioterapico, fitoterapico, venda
    ) -> None:
        self.__cliente_classe = cliente
        self.__laboratorio_classe = laboratorio
        self.__quimioterapico_classe = quimioterapico
        self.__fitoterapico_classe = fitoterapico
        self.__venda_classe = venda

