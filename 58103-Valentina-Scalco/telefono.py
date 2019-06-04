class Telefono:
    def __init__(self):
        self.llamada_ok = False
        self.credito = 0

    def agregar_credito(self, credito):
        self.credito += credito

    def dial(self, numero):
        if (len(numero) == 3 and (numero[0] == '9' or numero[0] == '8')):
            return True
    
        if (len(numero) == 7 and self.credito >= 10):
            self.credito -= 10
            return True

        if (numero[0] == '0' and numero[1] == '0' and self.credito >= 100):
            self.credito -= 100
            return True
        return False

 
