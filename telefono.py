class Telefono(object):

    
    def __init__(self):
        self.credito = 0
        self.llamada_ok = False
        
    
    
    def agregar_credito(self,credito):
       
        self.credito += credito
    
    def dial(self, numero):
       
        if len(numero) == 3:
            if (numero[0] == '9' or numero[0] == '8'):

                
                return True
            else:
                
                return False
        
        if len(numero) == 7:
           
            if self.credito < 10:

                return False

            else:

                self.credito -= 10
                return True
        
        
        if numero[0:2] == '00':

            if self.credito < 100:

                return False
            
            else:
            
                self.credito -= 100
            
            return True
