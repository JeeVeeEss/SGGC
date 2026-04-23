from Resistor import Resistor
from Capacitor import Capacitor

class Circuito:
    resistores = []
    capacitores = []
    __tensao_padrao = 220
    def __init__(self, tensao= __tensao_padrao):
        self.tensao = tensao
    def adicionar_componente(self, tipo, dados):
        if tipo == 'r' or tipo == 'R':
            self.resistores.append(dados)
        elif tipo == 'c' or tipo == 'C':
            self.capacitores.append(dados)

    def __str__(self):
        return f"Tensão do sistema: {self.tensao}\nNúmero de Resistores: {len(self.resistores)} - {str([ self.resistores[i].resistencia for i in range(len(self.resistores))])+" - (em Ω)"}\nNúmero de Capacitores: {len(self.capacitores)} - {str([ self.capacitores[i].capacitancia for i in range(len(self.capacitores))])+" - (em F)"}\n Reatância Capacitiva: {sum([self.capacitores[i].calcular_impedancia() for i in range(len(self.capacitores))])}"