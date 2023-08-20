class Controller:
    """
    Classe controladora que gerencia farmácia e interage com usuário
        para  cadastro de clientes, medicamentos, vendas
        e operações relacionadas.

    Atributos:
        cliente (class): Classe Cliente.
        laboratorio (class): Classe Laboratório.
        quimioterapico (class): Classe MedicamentoQuimioterapico.
        fitoterapico (class): Classe MedicamentoFitoterapico.
        venda (class): Classe Venda.
    """

    def __init__(
        self, cliente, laboratorio, quimioterapico, fitoterapico, venda
    ) -> None:
        """
        Inicializa uma instância de Controller.

        :param cliente: Cliente.
        :param laboratorio: Laboratorio.
        :param quimioterapico: MedicamentoQuimioterapico.
        :param fitoterapico: MedicamentoFitoterapico.
        :param venda: Venda.
        """
        self.__cliente_classe = cliente
        self.__laboratorio_classe = laboratorio
        self.__quimioterapico_classe = quimioterapico
        self.__fitoterapico_classe = fitoterapico
        self.__venda_classe = venda

    def __cadastrar_cliente(self):
        """
        Método privado que realiza o cadastro de um novo cliente.
        """
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

    def __cadastrar_laboratorio(self):
        """
        Método privado que realiza o cadastro de um novo laboratório,
            se ele não existir.
            Se ele já existir, retorna o laboratório encontrado.
        """
        nome = input("\nDigite o nome do laboratório: ")

        for (
            laboratorio_existente
        ) in self.__laboratorio_classe.laboratorios_cadastrados:
            if laboratorio_existente.nome == nome:
                print(f"\nO laboratório {nome} está cadastrado.")
                return laboratorio_existente
        print(
            "\nLaboratório não cadastrado, forneça as informações de cadastro:"
        )
        endereco = input("\nDigite o endereço do laboratório: ")
        telefone = input("\nDigite o telefone do laboratório: ")
        cidade = input("\nDigite a cidade do laboratório: ")
        estado = input("\nDigite o estado do laboratório: ")

        laboratorio = self.__laboratorio_classe(
            nome, endereco, telefone, cidade, estado
        )
        print(
            f"\nLaboratório {laboratorio.nome} foi cadastrado com sucesso!\n"
        )
        return laboratorio

    def __cadastrar_medicamento(self):
        """
        Método privado que realiza o cadastro de um novo medicamento.
        """
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

    def __listar_clientes(self):
        for cliente in self.__cliente_classe.listar_clientes:
            print(f"Nome: {cliente.nome};")
            print(f"CPF: {cliente.cpf};")
            print(f"Data de Nascimento: {cliente.data_nascimento}")

    def __consultar_cliente(self):
        cpf = input("Digite o CPF do cliente para consulta (sem pontuação): ")
        found = False
        for cliente in self.__cliente_classe.clientes_cadastrados:
            if cliente.cpf == cpf:
                print("\nInformações do Cliente:")
                print(f"Nome: {cliente.nome}")
                print(f"CPF: {cliente.cpf}")
                print("Data de Nascimento: ", end="")
                print({cliente.data_nascimento.strftime("%d-%m-%Y")})
                found = True
                break
            if not found:
                print(f"O cliente de CPF {cpf} não está cadastrado.")

    def __consultar_historico_compras(self):
        cpf = input("Digite o CPF do cliente para consulta (sem pontuação): ")
        found = False
        for venda in self.__venda_classe.vendas:
            if venda.cliente.cpf == cpf:
                print("\nCompra realizada em: ", end="")
                print({venda.data_hora.strftime("%Y-%m-%d %H:%M:%S")})
                print("\nProdutos:")
                for produto in venda.produtos:
                    print(f"{produto['nome']}, Preço: {produto['preco']}")
                print(f"Valor Total: {venda.valor_total:.2f}")
                found = True
        if not found:
            print("Nenhum histórico de compras encontrado para este CPF.")

    def __listar_medicamentos(self):
        """
        Lista todos os medicamentos em ordem alfabética,
            com opções de filtro por tipo de medicamento.

        :return: Lista com os  medicamentos encontrados.
        """
        print("Opções de listagem:")
        print("1. Todos os medicamentos")
        print("2. Somente quimioterápicos")
        print("3. Somente fitoterápicos")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            todos_medicamentos = (
                self.__quimioterapico_classe.medicamentos
                + self.__fitoterapico_classe.medicamentos
            )
            print(
                sorted(
                    todos_medicamentos,
                    key=lambda medicamento: medicamento.nome,
                )
            )
        elif opcao == "2":
            print(self.__quimioterapico_classe.medicamentos)
        elif opcao == "3":
            print(self.__fitoterapico_classe.medicamentos)
        else:
            print("Opção inválida.POr favor, tente novamente")

    def __consultar_medicamento(self):
        """
        Busca medicamentos por nome, fabricante ou descrição parcial
            de acordo com o tipo.

        :return: Lista com os medicamentos encontrados.
        """
        tipo = input(
            "Digite o tipo do medicamento (1 Quimioterápico, 2 Fitoterápico): "
        )

        while tipo != "1" and tipo != "2":
            tipo = input(
                "Digite um tipo válido. 1 Quimioterápico e 2 Fitoterápico: "
            )

        termo_busca = input("Digite o nome, fabricante ou descrição parcial: ")

        medicamentos_encontrados = []

        if tipo == "1":
            for medicamento in self.__quimioterapico_classe.medicamentos:
                if (
                    termo_busca.lower() in medicamento.nome.lower()
                    or termo_busca.lower()
                    in medicamento.laboratorio.nome.lower()
                    or termo_busca.lower() in medicamento.descricao.lower()
                ):
                    medicamentos_encontrados.append(medicamento)
        else:
            for medicamento in self.__fitoterapico_classe.medicamentos:
                if (
                    termo_busca.lower() in medicamento.nome.lower()
                    or termo_busca.lower()
                    in medicamento.laboratorio.nome.lower()
                    or termo_busca.lower() in medicamento.descricao.lower()
                ):
                    medicamentos_encontrados.append(medicamento)

        print(medicamentos_encontrados)

    def main(self):
        while True:
            print("\nMenu:\n")
            print("1. Cadastrar cliente")
            print("2. Cadastrar medicamento")
            print("3. Listar todos os clientes")
            print("4. Consultar cliente")
            print("5. Consultar histórico de vendas")
            print("6. Consultar idade para desconto")
            print("7. Listar medicamentos")
            print("8. Consultar medicamento")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                break
            elif opcao == "1":
                self.__cadastrar_cliente()
            elif opcao == "2":
                self.__cadastrar_medicamento()
            elif opcao == "3":
                self.__listar_clientes()
                pass
            elif opcao == "4":
                self.__consultar_cliente()
            elif opcao == "5":
                self.__consultar_historico_compras()
            elif opcao == "6":
                # consultar_idade_desconto(lista_clientes)
                pass
            elif opcao == "7":
                self.__listar_medicamentos()
            elif opcao == "8":
                self.__consultar_medicamento()
