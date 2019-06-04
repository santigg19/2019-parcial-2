import unittest
from printer import Printer


class TestTelefono(unittest.TestCase):

    def setUp(self):
        self.impresora = Printer()

    def test_impresora_disponible(self):
        self.assertTrue(self.impresora.printer_available())

    def test_agregar(self):        
        self.impresora.add_print_job('Printing example')
        self.assertEqual(self.impresora.queue_printer,['Printing example'])
    
    def test_imprimir(self):
        self.impresora.queue_printer = ['Printing example']
        self.impresora.print_job()
        self.assertTrue(self.impresora.printing)
        self.assertEqual(self.impresora.queue_printer,[])
    
    def test_nada_para_imprimir(self):
        self.impresora.print_job()
        self.assertTrue(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description,'nothing to print')
    
    def test_printer_reset(self):
        self.impresora.reset_printer()
        self.assertFalse(self.impresora.printing)
        self.assertFalse(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description,'')

if __name__ == '__main__':
   unittest.main()