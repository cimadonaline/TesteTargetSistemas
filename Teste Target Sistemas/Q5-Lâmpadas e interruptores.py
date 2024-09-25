class Lampada:
    def __init__(self):
        self.estado = 'desligada'
        self.quente = False

    def ligar(self):
        self.estado = 'ligada'
        self.quente = True # A lâmpada fica quente quando ligada

    def desligar(self):
        if self.estado == 'ligada':
            self.estado = 'desligada'
            self.quente = False # A lâmpada esfria após ser desligada

def identificar_lampadas():
    # Criando as lâmpadas
    lampada_A = Lampada()
    lampada_B = Lampada()
    lampada_C = Lampada()

    # Ligando o primeiro interruptor (A)
    lampada_A.ligar()
    print("Interruptor A: Ligado")

    # Esperar 10 minutos (simulado aqui como uma pausa)
    # Neste exemplo não temos uma pausa real para simplificar o código

    # Desligando o interruptor A
    lampada_A.desligar()
    print("Interruptor A: Desligado")

    # Ligando o segundo interruptor (B)
    lampada_B.ligar()
    print("Interruptor B: Ligado")

    # Terceiro interruptor (C) permanece desligado
    print("Interruptor C: Desligado")

    # Simulação e identificação das lâmpadas
    print("\nIdentificando as lâmpadas:")
    
    # Verificando os estados das lâmpadas
    if lampada_B.estado == 'ligada':
        print("A lâmpada A está apagada e fria.")
        print("A lâmpada B está acesa.")
        print("A lâmpada C está apagada e fria.")
    elif lampada_A.estado == 'desligada' and lampada_A.quente:
        print("A lâmpada A está apagada e quente.")
        print("A lâmpada B está acesa.")
        print("A lâmpada C está apagada e fria.")

identificar_lampadas()

#Resposta terminal
# Interruptor A: Ligado
# Interruptor A: Desligado
# Interruptor B: Ligado
# Interruptor C: Desligado

#Identificando as lâmpadas:
#A lâmpada A está apagada e fria.
#A lâmpada B está acesa.
#A lâmpada C está apagada e fria.