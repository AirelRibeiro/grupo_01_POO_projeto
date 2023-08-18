class Medicamento:
    """
    Classe que representa um medicamento genérico.
    """

    def __init__(
        self,
        nome: str,
        composto: str,
        laboratorio: str,
        descricao: str,
        preco: float,
    ):
        """
        Inicializa uma instância de Medicamento.

        :param nome: str.
        :param composto: str.
        :param laboratorio: str.
        :param descricao: str.
        :param preco: float.
        """
        self.__nome = nome
        self.__composto = composto
        self.__laboratorio = laboratorio
        self.__descricao = descricao
        self.__preco = preco

    def __repr__(self) -> str:
        return (
            f"{self.nome}\n"
            f"Composto: {self.composto}\n"
            f"Laboratorio: {self.laboratorio}\n"
            f"Descrição: {self.descricao}\n"
            f"Preço: {self.preco}"
        )

    def get_nome(self):
        """
        Recupera o nome do medicamento.

        :return: str.
        """
        return self.__nome

    def set_nome(self, nome):
        """
        Define o nome do medicamento.

        :param nome: str.
        """
        self.__nome = nome

    def get_composto(self):
        """
        Recupera o composto do medicamento.

        :return: str.
        """
        return self.__composto

    def set_composto(self, composto):
        """
        Define o composto do medicamento.

        :param composto: str.
        """
        self.__composto = composto

    def get_laboratorio(self):
        """
        Recupera o laboratório do medicamento.

        :return: str.
        """
        return self.__laboratorio

    def set_laboratorio(self, laboratorio):
        """
        Define o laboratório do medicamento.

        :param laboratorio: str.
        """
        self.__laboratorio = laboratorio

    def get_descricao(self):
        """
        Recupera a descrição do medicamento.

        :return: str.
        """
        return self.__descricao

    def set_descricao(self, descricao):
        """
        Define a descrição do medicamento.

        :param descricao: str.
        """
        self.__descricao = descricao

    def get_preco(self):
        """
        Recupera o preço do medicamento.

        :return: float.
        """
        return self.__preco

    def set_preco(self, preco):
        """
        Define o preço do medicamento.

        :param preco: float.
        """
        self.__preco = preco

    nome = property(get_nome, set_nome)
    composto = property(get_composto, set_composto)
    laboratorio = property(get_laboratorio, set_laboratorio)
    descricao = property(get_descricao, set_descricao)
    preco = property(get_preco, set_preco)


class MedicamentoQuimioterapico(Medicamento):
    """
    Classe que representa um medicamento quimioterápico,
        uma subclasse da classe Medicamento.
    """

    """ Lista para armazenar os medicamentos quimioterápicos criados """
    medicamentos = []

    def __init__(
        self, nome, composto, laboratorio, descricao, preco, necessita_receita
    ):
        """
        Inicializa uma instância de MedicamentoQuimioterapico.
        :param nome: str.
        :param composto: str.
        :param laboratorio: str.
        :param descricao: str.
        :param preco: float.
        :param necessita_receita: bool.
        """
        super().__init__(nome, composto, laboratorio, descricao, preco)
        self.__necessita_receita = necessita_receita
        self.__criar_medicamento(self)

    # Solução baseada em: https://cursos.alura.com.br/forum/
    # topico-operacao-sort-e-append-177423
    @classmethod
    def __criar_medicamento(cls, medicamento: "MedicamentoQuimioterapico"):
        """
        Adiciona um medicamento quimioterápico à lista de medicamentos,
            ordenada pelo nome.
        Esse método é chamado no método __init__,
            cada vez que uma classe é instanciada.

        :param medicamento: Instância de MedicamentoQuimioterapico
            a ser adicionada.
        """
        cls.medicamentos = sorted(
            cls.medicamentos + [medicamento], key=lambda x: x.nome
        )

    def __repr__(self) -> str:
        return (
            f"\n\n{self.nome}\n"
            f"Composto: {self.composto}\n"
            f"Laboratorio: {self.laboratorio}\n"
            f"Descrição: {self.descricao}\n"
            f"Preço: {self.preco}"
            f"Necessita receita? {'Sim' if self.necessita_receita else 'Não'}"
        )

    def get_necessita_receita(self):
        """
        Recupera necessita_receita,
            o atributo que informa se o medicamento
            precisa de receita para ser comprado

        :return: bool.
        """
        return self.__necessita_receita

    def set_necessita_receita(self, necessita_receita):
        """
        Define necessita_receita,
            o atributo que informa se o medicamento precisa
            de receita para ser comprado

        :param necessita_receita: bool.
        """
        self.__necessita_receita = necessita_receita

    necessita_receita = property(get_necessita_receita, set_necessita_receita)


class MedicamentoFitoterapico(Medicamento):
    """
    Classe que representa um medicamento fitoterápico.
    uma subclasse da classe Medicamento.
    """

    """ Lista para armazenar medicamentos criados """
    medicamentos = []

    def __init__(
        self,
        nome: str,
        composto: str,
        laboratorio: str,
        descricao: str,
        preco: float,
    ):
        """
        Inicializa uma instância de MedicamentoFitoterapico.

        :param nome: str.
        :param composto: str.
        :param laboratorio: str.
        :param descricao: str.
        :param preco: float.
        """
        super().__init__(nome, composto, laboratorio, descricao, preco)
        self.criar_medicamento(self)

    @classmethod
    def criar_medicamento(cls, medicamento: "MedicamentoFitoterapico"):
        """
        Adiciona um medicamento fitoterápico à lista de medicamentos,
            ordenada pelo nome.
        Esse método é chamado no método __init__,
            cada vez que uma classe é instanciada.

        :param medicamento: Instância de MedicamentoFitoterapico
            a ser adicionada.
        """
        cls.medicamentos = sorted(
            cls.medicamentos + [medicamento], key=lambda x: x.nome
        )
