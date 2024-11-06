class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro acelerou. Velocidade atual: {self.velocidade} km/h')

    def frear(self, decremento):
        if decremento >= self.velocidade:
            self.velocidade = 0
        else:
            self.velocidade -= decremento
        print(f'O carro freou. Velocidade atual: {self.velocidade} km/h')

    def exibir_velocidade(self):
        print(f'Velocidade atual: {self.velocidade} km/h')



carro = Carro("Fiat", "Uno")