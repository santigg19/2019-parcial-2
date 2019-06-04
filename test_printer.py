import unittest

from printer import Printer

class TestPrinter(unittest.TestCase):
    def setUp(self):
        self.imp = Printer()
    
    def test_impresora_ON(self):
        self.assertFalse(self.imp.printing)
        self.assertFalse(self.imp.error_flag)
        self.assertEqual(self.imp.error_description, "")

        self.assertTrue(self.imp.printer_available())
        self.assertEqual(self.imp.queue_printer, [])

    def test_impresion_OK(self):
        self.assertTrue(self.imp.printer_available())
        self.imp.add_print_job(['Hello world', 'Hello world 2'])
        self.imp.print_job()

        self.assertFalse(self.imp.error_flag)
        self.assertTrue(self.imp.printing)
        self.assertFalse(self.imp.printer_available())

        self.imp.reset_printer()
        self.assertTrue(self.imp.printer_available())
        self.assertFalse(self.imp.error_flag)


    def test_impresion_False(self):
        self.assertTrue(self.imp.printer_available())

        self.imp.print_job()

        self.assertTrue(self.imp.error_flag)
        self.assertEqual(self.imp.error_description, "no print")

        self.imp.reset_printer()
        self.assertTrue(self.imp.printer_available())
        self.assertFalse(self.imp.error_flag)

        


if __name__ == '__main__':
    unittest.main()

