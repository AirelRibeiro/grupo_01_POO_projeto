class Cliente:
    clientes_cadastrados = []

    def __init__(self, cpf, nome, data_nascimento):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.salvar_cliente(self)
    
    @classmethod
    def salvar_cliente(cls, cliente):
        cls.clientes_cadastrados.append(cliente)

    @staticmethod
    def vilida_cpf(cpf):
        pass

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        if self.valida_cpf(cpf):
            self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    cpf = property(get_cpf, set_cpf)
    nome = property(get_nome, set_nome)
    data_nascimento = property(get_data_nascimento, set_data_nascimento)
