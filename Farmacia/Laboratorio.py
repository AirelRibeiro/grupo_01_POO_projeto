class Laboratorio:
    laboratorios_cadastrados = []

    def __init__(self, nome, endereco, telefone, cidade, estado):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cidade = cidade
        self.__estado = estado
        self.salvar_lab(self)
    
    @classmethod
    def salvar_laboratorio(cls, lab):
        cls.laboratorios_cadastrados.append(lab)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_cidade(self):
        return self.__cidade

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    nome = property(get_nome, set_nome)
    endereco = property(get_endereco, set_endereco)
    telefone = property(get_telefone, set_telefone)
    cidade = property(get_cidade, set_cidade)
    estado = property(get_estado, set_estado)
