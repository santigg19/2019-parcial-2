class Telefono():
    
   def __init__(self):

      self.credito = 0

   def agregar_credito(self, cantidad):
       self.credito += cantidad

   def dial(self,numero):

       if len(numero) == 3:
           if numero[0] == "8" or numero[0] == "9":
               return True

       elif len(numero) == 7:
           if self.credito >= 10:
               self.credito -= 10
               return True

       elif numero[0]== "0" and numero[1]== "0":
           if self.credito >= 100:
               self.credito -= 100
               return True
       return False
              
            
