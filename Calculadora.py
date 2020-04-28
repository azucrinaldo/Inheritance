class Calculadora:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    def somar (self, i1, i2):
        print (i1 + i2)
    def subtrair (self, i1, i2):
        print (i1 - i2)
    def multiplicar (self, i1, i2):
        print (i1 * i2)
    def dividir (self, i1, i2):
        print (i1 / i2)