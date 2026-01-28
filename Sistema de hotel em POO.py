class Cliente:
    def __init__(self, nome: str, idade: int, documento: str, saldo: float, diasEstadia:int):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.saldo = saldo
        self.diasEstadia = diasEstadia
        self.hospedado = False

    def custoTotal(self, precodiaria):
        return  self.diasEstadia * precodiaria

    def __str__(self):
        status = "Hospedado" if self.hospedado else "Não hospedado"
        return f'{self.nome} - {self.documento}'

class Gerenciador_hotel:
    def __init__(self):
        self.listaClientes = [
            Cliente("Jonatas",25, "12345678945",  1000,  3),
            Cliente("Cauã", 19, "98765432147", 10000, 1)
        ]
        self.preco_diaria = 100

    def buscarCliente(self, identificacao, mostrar: bool = False):
        identificacao = str(identificacao).strip().lower()
        resposta = [cliente for cliente in self.listaClientes if cliente.documento == identificacao]
        return resposta[0] if resposta else None

    @staticmethod
    def validarCpfCliente(documento):
        return len(documento) == 11 and documento.isdigit()

    def criarCliente(self):
        print(f"Criando novo cliente.......")
        nome = input("Nome do cliente: ")
        idade = int(input("Idade: "))
        documento = input("CPF (somente número): ")

        if self.buscarCliente(documento):
            print("Já existe um cliente com esse documento")
            return

        if not self.validarCpfCliente(documento):
            print("CPF inválido")
            return
        dias = int(input("Dias que deseja ficar: \n"))
        saldo = float(input("Quanto você tem de saldo: \n"))
        novoCliente = Cliente(nome, idade, documento, saldo, dias)
        self.listaClientes.append(Cliente(nome, idade, documento, 0, 0))
        print("Cliente criado com sucesso!")

    def listarClientes(self):
        if not self.listaClientes:
            print("Lista vazia")
        else:
            for cliente in self.listaClientes:
                print(cliente)

    def removerCliente(self, documento):
        cliente = self.buscarCliente(documento)
        if cliente:
            self.listaClientes.remove(cliente)
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado")

    def atualizarCliente(self, documento):
        cliente = self.buscarCliente(documento)
        if not cliente:
            print("Cliente não encontrado")
        else:
            if cliente.idade < 18:
                print("Menor de idade não pode fazer check in sozinho!")
                return

            custo = cliente.custoTotal(self.precodiaria)
            if custo > cliente.saldo:
                print("Saldo insuficiente para realizar check in!")
                return
            cliente.hospedado = not cliente.hospedado

            acao = "CHECK IN" if cliente.hospedado else ("CHECK OUT")
            print(f"{acao} realizado com sucesso!")

hotel = Gerenciador_hotel

while True:
    print(f"\n{'-' * 20}\nSISTEMA DE HOTEL\n{'-' * 20}\n")
    try:
        escolha = int(input("Escolha: 1 - Criar | 2 - Buscar | 3 - Listar | 4 - Check-in/Check-out | 5 - Deletar | 6 - Sair: "))
        match escolha:
            case 1:
                hotel.criarCliente()
            case 2:
                hotel.buscarCliente(input("Informe o documento do cliente: "), mostrar = True)
            case 3:
                hotel.listarCliente()
            case 4:
                hotel.atualizarCliente(input("Informe o documento do cliente: "))
            case 5:
                hotel.removerCliente(input("Informe o documento do cliente: "))
            case 6:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida!")
    except ValueError:
        print("Erro, digite apenas números inteiros!")

