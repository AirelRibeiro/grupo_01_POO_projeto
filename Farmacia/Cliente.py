from datetime import datetime


class Cliente:
    """
    Classe que representa um cliente cadastrado.

    Atributos:
        cpf (str): CPF do cliente.
        nome (str): Nome do cliente.
        data_nascimento (str): Data de nascimento
            do cliente no formato 'dd/mm/aaaa'.
    """

    clientes_cadastrados = []

    def __init__(self, cpf: str, nome: str, data_nascimento: str) -> None:
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
        self.__salvar_cliente(self)

    @classmethod
    def __salvar_cliente(cls, cliente: "Cliente") -> None:
        """
        Adiciona um cliente à lista de clientes cadastrados.

        :param cliente: Instância de Cliente a ser cadastrada.
        """
        cls.clientes_cadastrados.append(cliente)

    @classmethod
    def listar_clientes(cls):
        """
        Lista todos os clientes cadastrados em ordem alfabética.

        :return: Lista de instâncias de Cliente em ordem alfabética.
        """
        return sorted(
            cls.clientes_cadastrados, key=lambda cliente: cliente.nome
        )

    @staticmethod
    def valida_cpf(cpf: str) -> bool:
        """
        Verifica se o CPF a ser cadastrado é válido.

        :param cpf: CPF a ser validado (str).
        :return: True se o CPF for válido e False caso contrário.
        """
        cpf = cpf.replace(".", "").replace(
            "-", ""
        )  # Isso remove os pontos e o hífen
        if not cpf.isdigit() or len(cpf) != 11:
            return False

        # Verificando os dígitos
        total = 0
        for i in range(9):
            total += int(cpf[i]) * (10 - i)
        remainder = total % 11
        digit1 = 0 if remainder < 2 else 11 - remainder

        total = 0
        for i in range(10):
            total += int(cpf[i]) * (11 - i)
        remainder = total % 11
        digit2 = 0 if remainder < 2 else 11 - remainder

        return cpf[-2:] == str(digit1) + str(digit2)

    @staticmethod
    def valida_data_nascimento(data_nascimento: str) -> bool:
        """
        Valida uma data de nascimento no formato 'dd/mm/aaaa'
        e verifica se o cliente tem mais de 18 anos.

        :param data_nascimento: str.
        :return: True se a data é válida e o cliente tem mais de 18 anos,
            False caso contrário.
        """
        # Validação de data consultade em: https://shre.ink/valida-data-python
        try:
            dia, mes, ano = map(int, data_nascimento.split("/"))
            if mes < 1 or mes > 12 or ano <= 0:
                return False

            if mes in (1, 3, 5, 7, 8, 10, 12):
                ultimo_dia = 31
            elif mes == 2:
                if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                    ultimo_dia = 29
                else:
                    ultimo_dia = 28
            else:
                ultimo_dia = 30

            if dia < 1 or dia > ultimo_dia:
                return False

            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.today()
            idade = (
                hoje.year
                - data.year
                - ((hoje.month, hoje.day) < (data.month, data.day))
            )

            if idade >= 18:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_cpf(self) -> str:
        """
        Obtém o CPF do cliente.

        :return: CPF do cliente (str).
        """
        return self.__cpf

    def set_cpf(self, cpf: str) -> None:
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

    def set_nome(self, nome: str) -> None:
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

    def set_data_nascimento(self, data_nascimento: str) -> None:
        """
        Define a data de nascimento do cliente.

        :param data_nascimento: Nova data de nascimento do cliente
            no formato 'dd/mm/aaaa' (str).
        """
        self.__data_nascimento = data_nascimento

    cpf = property(get_cpf, set_cpf)
    nome = property(get_nome, set_nome)
    data_nascimento = property(get_data_nascimento, set_data_nascimento)
