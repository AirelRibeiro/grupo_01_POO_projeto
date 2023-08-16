class Medicamento:
    def __init__(self, nome, composto, laboratorio, descricao, preco):
        self.__nome = nome
        self.__composto = composto
        self.__laboratorio = laboratorio
        self.__descricao = descricao
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_composto(self):
        return self.__composto

    def set_composto(self, composto):
        self.__composto = composto

    def get_laboratorio(self):
        return self.__laboratorio

    def set_laboratorio(self, laboratorio):
        self.__laboratorio = laboratorio

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    nome = property(get_nome, set_nome)
    composto = property(get_composto, set_composto)
    laboratorio = property(get_laboratorio, set_laboratorio)
    descricao = property(get_descricao, set_descricao)
    preco = property(get_preco, set_preco)


class MedicamentoQuimioterapico(Medicamento):
    def __init__(
        self, nome, composto, laboratorio, descricao, preco, necessita_receita
    ):
        super().__init__(nome, composto, laboratorio, descricao, preco)
        self.__necessita_receita = necessita_receita

    def get_necessita_receita(self):
        return self.__necessita_receita

    def set_necessita_receita(self, necessita_receita):
        self.__necessita_receita = necessita_receita

    necessita_receita = property(get_necessita_receita, set_necessita_receita)


class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome, composto, laboratorio, descricao, preco):
        super().__init__(nome, composto, laboratorio, descricao, preco)
