from ComponenteEletrico import ComponenteEletrico
import math
class Capacitor(ComponenteEletrico):
    def __init__(self, nome, fabricante, capacitancia = 1):
        super().__init__(nome, fabricante, tensao_max=None) # Método para inicializar as variáveis herdadas pelo ComponenteEletrico
        self.capacitancia = capacitancia

    def calcular_impedancia(self):
        
        impedancia = 1/(2*math.pi*60*int(self.capacitancia))
        return impedancia
           
    def __str__(self):
        return self.nome, self.fabricante, self.capacitancia
    
