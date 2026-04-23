from Circuito import Circuito
from Capacitor import Capacitor
from Resistor import Resistor
import platform
import os

#verificar o sistema operac.
sys = platform.system()
def limpador(sys):
    try:
        if sys == "Darwin" or sys == "darwin":
            os.system('clear')
        elif sys == "Windows":
            os.system('cls')
        elif sys == "Linux":
            os.system("clear")
        else:
            print("---------------------")    
    except Exception:
        print("---------------------")

def configurar_circuito():
    try: 
        obj = int(input("Digite a tensão do circuito: "))
        return obj
    except ValueError:
        return 220

def validar_dado(valor:None):
    if valor:
        pass
    else:
        raise TypeError('Valor inválido. Tente novamente')
def main():
    limpador(sys)
    tensao = configurar_circuito()
    circuito = Circuito(tensao=tensao)

    while True:
        #limpador(sys)
        print("-------------\n-R(resistor)\n-C(capacitor)\n-X(Sair do programa)")
        operacao = str(input("Digite o componente a ser adicionado ao sistema: "))
        if operacao == 'X' or operacao == 'x':
            break
        elif operacao == 'c' or operacao == 'C':
            limpador(sys)
            dados = ""
            dados  = str(input('Digite os dados: \n- Nome do Componente.\n- Nome do Fabricante.\n- Valor(ohms/farads), respectivamente(exemplo: q q 23)\n(Em caso de Valores nulos, os atributos serão nulos, menos o valor que será 1): ')) or "   "
            limpador(sys)
            if dados:
                dados = dados.split(' ')
            else: 
                dados = 1
            circuito.adicionar_componente(operacao, Capacitor(dados[0], dados[1], dados[2]))
        elif operacao == 'r' or operacao == 'R':
            limpador(sys)
            dados = ""
            try:
                dados  = str(input('Digite os dados: \n- Nome do Componente.\n- Nome do Fabricante.\n- Valor(ohms/farads), respectivamente: ')) or '   '
                #limpador(sys)
                if dados:
                    dados = dados.split(' ')
                    try:
                        circuito.adicionar_componente(operacao, Resistor(dados[0], dados[1], dados[2]))
                    except IndexError:
                        print(len(dados), dados)
            except ValueError:
                dados = 1
                circuito.adicionar_componente(operacao, Resistor('', '', dados))
        print(circuito) # Apenas para teste, sem função estrutural.
main()