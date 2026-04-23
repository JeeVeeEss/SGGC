from Resistor import Resistor
from Capacitor import Capacitor

class Circuito:
    resistores = []
    capacitores = []
    def __init__(self, tensao= 220):
        self.tensao = tensao
    def adicionar_componente(self, tipo, dados):
        if tipo == 'r' or tipo == 'R':
            self.resistores.append(dados)
        elif tipo == 'c' or tipo == 'C':
            self.capacitores.append(dados)

    def __str__(self):
        return f"Tensão do sistema: {self.tensao}\nNúmero de Resistores: {len(Circuito.resistores)}\nNúmero de Capacitores: {len(Circuito.capacitores)}"