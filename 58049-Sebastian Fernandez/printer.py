#Administración manual de impresora

class Printer:

    def __init__(self):

        self.queue_printer = []

        self.printing = False

        self.error_flag = False

        self.error_description = ""



    # Imprime el primer trabajo de la lista siempre que haya algo en la lista

    def print_job(self):

        if len(self.queue_printer) == 0:

            self.error_flag = True

            self.error_description = "nothing to print"

            return



        self.printing = True

        self.queue_printer.pop(0)


    # Hay que llamar esta función para liberar la impresora luego de terminar de imprimir

    # También debe usarse para liberar a la impresora de un error

    def reset_printer(self):

        self.printing = False

        self.error_flag = False

        self.error_description = ""