class Laboratorio:
    """
    Classe que representa um laboratório cadastrado.

    Atributos:
        nome (str): Nome do laboratório.
        endereco (str): Endereço (rua e bairro) do laboratório.
        telefone (str): Número de telefone do laboratório.
        cidade (str): Cidade do laboratório.
        estado (str): Estado do laboratório.
    """

    laboratorios_cadastrados = []

    def __init__(
        self, nome: str, endereco: str, telefone: str, cidade: str, estado: str
    ):
        """
        Inicializa uma instância de Laboratorio.

        :param nome: str.
        :param endereco: str.
        :param telefone: str.
        :param cidade: str.
        :param estado: str.
        """
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cidade = cidade
        self.__estado = estado
        self.salvar_laboratorio(self)

    @classmethod
    def salvar_laboratorio(cls, lab: "Laboratorio") -> None:
        """
        Adiciona um laboratório à lista de laboratórios cadastrados.

        :param lab: Instância de Laboratorio a ser cadastrada.
        """
        cls.laboratorios_cadastrados.append(lab)

    def get_nome(self) -> str:
        """
        Obtém o nome do laboratório.

        :return: Nome do laboratório (str).
        """
        return self.__nome

    def set_nome(self, nome: str) -> None:
        """
        Define o nome do laboratório.

        :param nome: Novo nome do laboratório (str).
        """
        self.__nome = nome

    def get_endereco(self) -> str:
        """
        Obtém o endereço do laboratório.

        :return: Endereço do laboratório (str).
        """
        return self.__endereco

    def set_endereco(self, endereco: str) -> None:
        """
        Define o endereço do laboratório.

        :param endereco: Novo endereço do laboratório (str).
        """
        self.__endereco = endereco

    def get_telefone(self) -> str:
        """
        Obtém o número de telefone do laboratório.

        :return: Número de telefone do laboratório (str).
        """
        return self.__telefone

    def set_telefone(self, telefone: str) -> None:
        """
        Define o número de telefone do laboratório.

        :param telefone: Novo número de telefone do laboratório (str).
        """
        self.__telefone = telefone

    def get_cidade(self) -> str:
        """
        Obtém a cidade do laboratório.

        :return: Cidade do laboratório (str).
        """
        return self.__cidade

    def set_cidade(self, cidade: str) -> None:
        """
        Define a cidade do laboratório.

        :param cidade: Nova cidade do laboratório (str).
        """
        self.__cidade = cidade

    def get_estado(self) -> str:
        """
        Obtém o estado do laboratório.

        :return: Estado do laboratório (str).
        """
        return self.__estado

    def set_estado(self, estado: str) -> None:
        """
        Define o estado do laboratório.

        :param estado: Novo estado do laboratório (str).
        """
        self.__estado = estado

    nome = property(get_nome, set_nome)
    endereco = property(get_endereco, set_endereco)
    telefone = property(get_telefone, set_telefone)
    cidade = property(get_cidade, set_cidade)
    estado = property(get_estado, set_estado)
