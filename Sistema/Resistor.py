from ComponenteEletrico import ComponenteEletrico

class Resistor(ComponenteEletrico):
    def __init__(self, nome, fabricante ,resistencia):
        super().__init__( nome, fabricante) # Método para inicializar as variáveis herdadas pelo ComponenteEletrico
        self.resistencia = resistencia
