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

    def __cadastrar_medicamento(self):
        nome = input("Digite o nome do medicamento: ")
        principal_composto = input(
            "Digite o principal composto do medicamento: "
        )
        descricao = input("Digite uma descrição para o medicamento: ")

        for index, lab in enumerate(
            self.__laboratorio_classe.laboratorios_cadastrados
        ):
            print(f"{index + 1}: {lab.nome}")
        lab_index = int(input("Escolha o laboratório pelo número: "))
        laboratorio = self.__laboratorio_classe.laboratorios_cadastrados[
            lab_index - 1
        ]

        tipo = input(
            "Digite o tipo do medicamento (1 Quimioterápico, 2 Fitoterápico): "
        )

        while tipo != "1" and tipo != "2":
            tipo = input(
                "Digite um tipo válido. 1  Quimioterápico e  2 Fitoterápico): "
            )

        if tipo == "1":
            necessita_receita = input(
                "O medicamento necessita de receita? (S - sim, N - não): "
            )
            necessita_receita = (
                True if necessita_receita.upper() == "S" else False
            )
            self.__quimioterapico_classe(
                nome,
                principal_composto,
                laboratorio,
                descricao,
                necessita_receita,
            )
        else:
            self.__fitoterapico_classe(
                nome, principal_composto, laboratorio, descricao
            )

        print(f"Medicamento {nome} cadastrado com sucesso!")

