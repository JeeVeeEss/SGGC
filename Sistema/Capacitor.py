from ComponenteEletrico import ComponenteEletrico
class Capacitor(ComponenteEletrico):
    def __init__(self, nome, fabricante, capacitancia):
        super().__init__(nome, fabricante, tensao_max=None) # Método para inicializar as variáveis herdadas pelo ComponenteEletrico
        self.capacitancia = capacitancia

    def calcular_impedancia(self):
        impedancia = 1/(2*(3,1415)*60*self.capacitancia)
    
    def __str__(self):
        return self.nome, self.fabricante, self.capacitancia[0].capacitancia