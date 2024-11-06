class pessoa: 
    def _init_(self, nome,  email, senha):
        self.nome = nome
        self._email = email 
        self.__senha = senha

    def apresentar(self):
        print(self.nome, self.email, self._senha)

pessoa1 = pessoa ("Felipe", "felipe@hotmail" , 999)
print (pessoa1.nome)
print (pessoa1._email)
print (pessoa1.__senha)
pessoa1.apresentar()