from Circuito import Circuito
from Capacitor import Capacitor
from Resistor import Resistor
import os

def configurar_circuito():
    obj = str(input("Digite a tensão do circuito: "))
    return obj

def main():
    os.system('cls')
    tensao = configurar_circuito()
    circuito = Circuito(tensao=tensao)

    while True:
        #os.system('cls')
        print("-------------\n-R(resistor)\n-C(capacitor)\n-X(Sair do programa)")
        operacao = str(input("Digite o componente a ser adicionado ao sistema (nome e fabricante) separados por espaço(" ") : "))
        if operacao == 'X' or operacao == 'x':
            break
        elif operacao == 'c' or operacao == 'C':
            dados  = str(input('Digite o valor desejado( Resistência(ohms)/ Capacitância(faraday):'))
            dados = dados.split(' ')
            circuito.adicionar_componente(operacao, Capacitor(dados[0], dados[1], dados[2]))
        elif operacao == 'r' or operacao == 'R':
            circuito.adicionar_componente(operacao, Resistor(dados[0], dados[1], dados[2]))
        print(circuito, circuito.resistores, circuito.capacitores) # Apenas para teste, sem função estrutural.
main()