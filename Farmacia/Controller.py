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

    def __realizar_venda(self):
        """
        Método privado que realiza uma venda.
        """
        cpf = input("Digite o CPF do cliente (sem pontuação): ")

        cliente = None
        for cliente_existente in self.__cliente_classe.clientes_cadastrados:
            if cliente_existente.cpf == cpf:
                cliente = cliente_existente
                break

        if cliente is None:
            print("Cliente não cadastrado. Realize o cadastro agora!")
            cliente = self.__cadastrar_cliente()

        produtos = []
        while True:
            nome_produto = input(
                "Digite o nome do produto ou 'fim' para encerrar: "
            )
            if nome_produto.lower() == "fim":
                break

            produto_encontrado = False
            for produto in (
                self.__quimioterapico_classe.medicamentos
                + self.__fitoterapico_classe.medicamentos
            ):
                if produto.nome.lower() == nome_produto.lower():
                    if (
                        isinstance(produto, self.__quimioterapico_classe)
                        and produto.necessita_receita is True
                    ):
                        print("Medicamento controlado!\n")
                        print(f"Verificar a receita para {produto.nome}\n")
                    produtos.append(produto)
                    produto_encontrado = True
                    break

            if not produto_encontrado:
                print(f"\nProduto '{nome_produto}' não encontrado.\n")

        if not produtos:
            print("\nNenhum produto adicionado à lista de compra.\n")
            return

        venda = self.__venda_classe(produtos, cliente)
        print("\nVenda realizada com sucesso!\n")
        print(list(produto.nome for produto in venda.produtos))

        if venda.houve_desconto is True:
            print(f"\nDesconto de {venda.desconto}.\n")
        print(f"\nValor total: {venda.valor_total}\n")

    def __cadastrar_cliente(self):
        """
        Método privado que realiza o cadastro de um novo cliente.
        """
        cpf = input("\nDigite o CPF do cliente (sem pontuação): ")
        if not self.__cliente_classe.valida_cpf(cpf):
            print(
                "\nCPF inválido. Por favor, tente novamente com um CPF válido."
            )
            return

        nome = input("\nDigite o nome do cliente: ")

        ano = input(
            "\nDigite o ano de nascimento do cliente com quatro dígitos: "
        )
        mes = input(
            "\nDigite o mês de nascimento do cliente com dois dígitos: "
        )
        dia = input(
            "\nDigite o dia de nascimento do cliente com dois dígitos: "
        )
        if not self.__cliente_classe.valida_data_nascimento(
            f"{dia}/{mes}/{ano}"
        ):
            print("Data inválida ou cliente com idade insuficiente.", end=" ")
            print("Por favor verifique os dados e tente novamente.")
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
        nome = input("\nDigite o nome do medicamento: ")
        principal_composto = input(
            "Digite o principal composto do medicamento: "
        )
        descricao = input("\nDigite uma descrição para o medicamento: ")

        laboratorio = self.__cadastrar_laboratorio()

        preco = float(input("\nDigite o preço desse medicamento: "))

        tipo = input(
            "\nDigite tipo de medicamento. 1 Quimioterápico, 2 Fitoterápico: "
        )

        while tipo != "1" and tipo != "2":
            tipo = input(
                "\nDigite um tipo válido.1 Quimioterápico e 2 Fitoterápico): "
            )

        if tipo == "1":
            necessita_receita = input(
                "\nO medicamento necessita de receita? (S - sim, N - não): "
            )
            necessita_receita = (
                True if necessita_receita.upper() == "S" else False
            )
            self.__quimioterapico_classe(
                nome,
                principal_composto,
                laboratorio,
                descricao,
                preco,
                necessita_receita,
            )
        else:
            self.__fitoterapico_classe(
                nome, principal_composto, laboratorio, descricao, preco
            )

        print(f"\nMedicamento {nome} cadastrado com sucesso!\n")

    def __listar_clientes(self):
        for cliente in self.__cliente_classe.listar_clientes():
            print(f"\nNome: {cliente.nome};")
            print(f"CPF: {cliente.cpf};")
            print(f"Data de Nascimento: {cliente.data_nascimento}")

    def __consultar_cliente(self):
        cpf = input(
            "\nDigite o CPF do cliente para consulta (sem pontuação): "
        )
        found = False
        for cliente in self.__cliente_classe.clientes_cadastrados:
            if cliente.cpf == cpf:
                print("\nInformações do Cliente:\n")
                print(f"Nome: {cliente.nome}")
                print(f"CPF: {cliente.cpf}")
                print("Data de Nascimento: ", end="")
                print(cliente.data_nascimento)
                found = True
                break
        if not found:
            print(f"\nO CPF {cpf} não está cadastrado.")

    def __consultar_historico_compras(self):
        cpf = input(
            "\nDigite o CPF do cliente para consulta (sem pontuação): "
        )
        found = False
        for venda in self.__venda_classe.vendas:
            if venda.cliente.cpf == cpf:
                print("\nCompra realizada em: ", end="")
                print({venda.data_hora.strftime("%Y-%m-%d %H:%M:%S")})
                print("\nProdutos:")
                for produto in venda.produtos:
                    print(f"\nProduto: {produto.nome}, Preço: {produto.preco}")
                print(f"\nValor Total: {venda.valor_total:.2f}")
                found = True
        if not found:
            print("\nNenhum histórico de compras encontrado para este CPF.")

    def __consultar_idade_desconto(self):
        cpf = input("\nDigite o CPF para consultar desconto (sem pontuação): ")
        found = False
        for cliente in self.__cliente_classe.clientes_cadastrados:
            if cliente.cpf == cpf:
                if self.__cliente_classe.valida_se_idoso(
                    cliente.data_nascimento
                ):
                    print("\nCliente tem direito a 15% de desconto.")
                else:
                    print("\nCliente não tem direito a desconto.")
                found = True
                break
        if not found:
            print(f"\nO CPF {cpf} não está cadastrado.")

    def __listar_medicamentos(self):
        """
        Lista todos os medicamentos em ordem alfabética,
            com opções de filtro por tipo de medicamento.

        :return: Lista com os  medicamentos encontrados.
        """
        print("\nOpções de listagem:")
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
            print("\nOpção inválida. Por favor, tente novamente.")

    def __consultar_medicamento(self):
        """
        Busca medicamentos por nome, fabricante ou descrição parcial
            de acordo com o tipo.

        :return: Lista com os medicamentos encontrados.
        """
        tipo = input(
            "\nDigite tipo de medicamento. 1 Quimioterápico, 2 Fitoterápico: "
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

    def __gera_relatorio_vendas(self):

        (
            total_vendas,
            total_receita,
            produto_mais_vendido,
            total_clientes,
            total_vendas_quimioterapico,
            total_vendas_fitoterapico,
        ) = self.__venda_classe.gerar_relatorio_vendas()

        print("\n\nRelatório de Vendas\n\n")
        print(f"\Total de Vendas: {total_vendas}\n")
        print(f"Total de Receita: R${total_receita:.2f}\n")
        print(f"Produto Mais Vendido: {produto_mais_vendido}\n")
        print(f"Total de Clientes Atendidos: {total_clientes}\n")
        print("Total de Vendas de Produtos Quimioterápicos:", end=" ")
        print(total_vendas_quimioterapico)
        print("\nTotal de Vendas de Produtos Fitoterápicos:", end=" ")
        print(total_vendas_fitoterapico)

    def main(self):
        count = 0
        while True:
            print("\nMenu:\n")
            print("1. Cadastrar cliente")
            print("2. Cadastrar medicamento")
            print("3. Cadastrar laboratório")
            print("4. Listar todos os clientes")
            print("5. Consultar cliente")
            print("6. Consultar histórico de vendas")
            print("7. Consultar idade para desconto")
            print("8. Listar medicamentos")
            print("9. Consultar medicamento")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                self.__gera_relatorio_vendas()
                break
            elif opcao == "1":
                self.__cadastrar_cliente()
            elif opcao == "2":
                self.__cadastrar_medicamento()
            elif opcao == "3":
                self.__cadastrar_laboratorio()
            elif opcao == "4":
                self.__listar_clientes()
                pass
            elif opcao == "5":
                self.__consultar_cliente()
            elif opcao == "6":
                self.__consultar_historico_compras()
            elif opcao == "7":
                self.__consultar_idade_desconto()
                pass
            elif opcao == "8":
                self.__listar_medicamentos()
            elif opcao == "9":
                self.__consultar_medicamento()
            else:
                count += 1
                if count < 5:
                    print("\nVocê precisa selecionar uma opção válida.\n")

                else:
                    print("\nSistema encerrado. Muitas interações inválidas!")
                    break
