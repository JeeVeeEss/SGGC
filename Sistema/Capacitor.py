from ComponenteEletrico import ComponenteEletrico
class Capacitor(ComponenteEletrico):
    def __init__(self, nome, fabricante, capacitancia):
        super().__init__(nome, fabricante) # Método para inicializar as variáveis herdadas pelo ComponenteEletrico
        self.capacitancia = capacitancia
        