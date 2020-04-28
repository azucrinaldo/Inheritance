from Calculadora import Calculadora


class CalcCientifica(Calculadora):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo, cor)
    def exponenciar(self, i1, i2):
        print(i1 ** i2)
