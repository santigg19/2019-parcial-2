import unittest
from printer import Printer


class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.impresora = Printer()

    def test_printer_disp(self):
        self.assertTrue(self.impresora.printer_available())
        
    def test_printer_no_disp(self):
        self.impresora.printing = True
        self.assertFalse(self.impresora.printer_available())

    def test_add_print_job(self):
        self.impresora.add_print_job ('Imprimiendo')
        self.assertEqual(self.impresora.queue_printer, ['Imprimiendo'])

    def test_adding_print_job(self):
        self.impresora.queue_printer = ['Imprimiendo']
        self.impresora.print_job()
        self.assertTrue(self.impresora.printing)
        self.assertEqual(self.impresora.queue_printer, [])

    def test_print_nothing(self):
        self.impresora.print_job()
        self.assertTrue(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description, "nothing to print")

    def test_reset_printer(self):
        self.impresora.reset_printer()
        self.assertFalse(self.impresora.printing)
        self.assertFalse(self.impresora.error_flag)
        self.assertEqual(self.impresora.error_description, "")
   


if __name__ == '__main__':
   unittest.main()
