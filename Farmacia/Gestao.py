class Controller:
    def __init__(
        self, cliente, laboratorio, quimioterapico, fitoterapico, venda
    ) -> None:
        self.__cliente_classe = cliente
        self.__laboratorio_classe = laboratorio
        self.__quimioterapico_classe = quimioterapico
        self.__fitoterapico_classe = fitoterapico
        self.__venda_classe = venda

    def __cadastrar_cliente(self):
        cpf = input("Digite o CPF do cliente (sem pontuação): ")
        if not self.__cliente_classe.validar_cpf(cpf):
            print(
                "CPF inválido. Por favor, tente novamente com um CPF válido."
            )
            return

        nome = input("Digite o nome do cliente: ")

        ano = input("Digite o ano de nascimento do cliente com dois dígitos")

        mes = input("Digite o mês de nascimento do cliente com dois dígitos")
        dia = input("Digite o dia de nascimento do cliente com dois dígitos")
        if not self.__cliente_classe.valida_data_nascimento(
            f"{dia}/{mes}/{ano}"
        ):
            print(
                "Data inválida ou cliente com idade insuficiente.",
                "Por favor verifique os dados e tente novamente.",
            )
            return

        cliente = self.__cliente_classe(cpf, nome, f"{dia}/{mes}/{ano}")
        print(f"Cliente {cliente.nome} foi cadastrado com sucesso!")
