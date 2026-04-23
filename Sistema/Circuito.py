from Resistor import Resistor
from Capacitor import Capacitor
from Style import Style

class Circuito:
    __resistores = []
    __capacitores = []
    __tensao_padrao = 220
    def __init__(self, tensao=__tensao_padrao):
        self.tensao = tensao
    def adicionar_componente(self, tipo, dados):
        if tipo == 'r' or tipo == 'R':
            self.__resistores.append(dados)
        elif tipo == 'c' or tipo == 'C': 
            if dados.capacitancia == '' or dados.capacitancia == [' ']:
                dados.capacitancia = 1
                self.__capacitores.append(dados)
            else:
                self.__capacitores.append(dados)

    def __str__(self):
        return f"Tensão do sistema: {Style.f_b_branco}{self.tensao}{Style.reset}\nNúmero de Resistores: {Style.u_branca}{len(self.__resistores)}{Style.reset} - {str([ self.__resistores[i].resistencia for i in range(len(self.__resistores))])+" - (em Ω)"}\nNúmero de Capacitores: {Style.u_branca}{len(self.__capacitores)}{Style.reset} - {str([ self.__capacitores[i].capacitancia for i in range(len(self.__capacitores))])+" - (em F)"}\n- Reatância Capacitiva: [{Style.f_verde}{sum([self.__capacitores[i].calcular_impedancia() for i in range(len(self.__capacitores))])}]{Style.reset}\n- Impedância de Resistores (em série):{Style.f_verde}{[self.__resistores[x].resistencia for x in range(len(self.__resistores))]}{Style.reset}\n- Impedância de Resistores (em paralelo): [{Style.f_verde}{sum([ int(self.__resistores[x].resistencia)**(-1) for x in range(len(self.__resistores))])}{Style.reset}]"