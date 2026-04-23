from ComponenteEletrico import ComponenteEletrico

class Resistor(ComponenteEletrico):
    def __init__(self, nome, fabricante ,resistencia):
        super().__init__( nome, fabricante, tensao_max=None) # Método para inicializar as variáveis herdadas pelo ComponenteEletrico
        self.resistencia = int(resistencia)
        if resistencia == '' or resistencia == '   ':
            self.resistencia = 1

    def __add__(self, resistor_n): # Método alternativo para calcular a impedância resistiva
        resistor_eq = self.resistencia + resistor_n.resistencia
        return resistor_eq

    
        