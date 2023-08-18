class Cliente:
    """
    Classe que representa um cliente cadastrado.

    Atributos:
        cpf (str): CPF do cliente.
        nome (str): Nome do cliente.
        data_nascimento (str): Data de nascimento do cliente
            no formato 'dd/mm/aaaa'.
    """

    clientes_cadastrados = []

    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        """
        Inicializa uma instância de Cliente.

        :param cpf: CPF do cliente (str).
        :param nome: Nome do cliente (str).
        :param data_nascimento: Data de nascimento do cliente
            no formato 'dd/mm/aaaa' (str).
        """
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.salvar_cliente(self)

    @classmethod
    def salvar_cliente(cls, cliente: "Cliente"):
        """
        Adiciona um cliente à lista de clientes cadastrados.

        :param cliente: Instância de Cliente a ser cadastrada.
        """
        cls.clientes_cadastrados.append(cliente)

    @staticmethod
    def valida_cpf(cpf: str):
        """
        Valida um CPF.

        :param cpf: CPF a ser validado (str).
        """
        pass  # Implementação da validação do CPF

    def get_cpf(self) -> str:
        """
        Obtém o CPF do cliente.

        :return: CPF do cliente (str).
        """
        return self.__cpf

    def set_cpf(self, cpf: str):
        """
        Define o CPF do cliente, se o CPF for válido.

        :param cpf: Novo CPF do cliente (str).
        """
        if self.valida_cpf(cpf):
            self.__cpf = cpf

    def get_nome(self) -> str:
        """
        Obtém o nome do cliente.

        :return: Nome do cliente (str).
        """
        return self.__nome

    def set_nome(self, nome: str):
        """
        Define o nome do cliente.

        :param nome: Novo nome do cliente (str).
        """
        self.__nome = nome

    def get_data_nascimento(self) -> str:
        """
        Obtém a data de nascimento do cliente.

        :return: Data de nascimento do cliente no formato 'dd/mm/aaaa' (str).
        """
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento: str):
        """
        Define a data de nascimento do cliente.

        :param data_nascimento: Nova data de nascimento do cliente
            no formato 'dd/mm/aaaa' (str).
        """
        self.__data_nascimento = data_nascimento

    cpf = property(get_cpf, set_cpf)
    nome = property(get_nome, set_nome)
    data_nascimento = property(get_data_nascimento, set_data_nascimento)
