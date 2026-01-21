nome = input("Informe seu nome:")
idade = input("Informe sua idade:")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá sou {self.nome} e tenho {self.idade} anos de idade!")

    class Carro:
        def __init__(self, marca, modelo, ano, cor):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
            self.cor = cor

        def ligarMotor(self):
            print(f"Ligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

        def desligarMotor(self):
            print(f"Desligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

    meuCarro = Carro("Toyota", "Corolla", 2020, "Prata")

    meuCarro.ligarMotor()

    carroDoAmigo = Carro("Honda", "Civic", 2019, "Preto")
    carroDoAmigo.ligarMotor()