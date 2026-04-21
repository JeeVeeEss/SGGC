from ComponenteEletrico import ComponenteEletrico

class Resistor(ComponenteEletrico):
    def __init__(self, nome, fabricante ,resistencia):
        super().__init__( nome, fabricante)
        self.resistencia = resistencia
