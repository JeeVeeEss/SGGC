class ComponenteEletrico:
    # nome, fabricante, tensao
    def __init__(self, nome, fabricante, tensao_max):
        self.nome = nome
        self.fabricante = fabricante
        self.tensao_max = tensao_max
        print('''
              Circuito iniciado!
              ''')
