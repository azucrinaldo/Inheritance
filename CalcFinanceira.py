from Calculadora import Calculadora


class CalcFinanceira(Calculadora):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo, cor)
    def modular(self, i1, i2):
        print(i1 % i2)