class carro: 
    def _init_(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def apresentar(self):
        print(self.marca, self.modelo, self.velocidade)

carro1 = carro ("ma","ja")
print (carro1.marca)
print (carro1.modelo)
carro1.apresentar()

velocidade = int(input("quantas vezes vc quer acelerar ?"))
