import unittest
from printer import Printer

class TestPrinter(unittest.TestCase):

    def test_disponibilidad_si(self):

        self.printing = False

        self.assertFalse(self.printing)
   
    def test_disponibilidad_no(self):
        self.printing = True
        self.assertTrue(self.printing)
        #try:
            #self.assertTrue(self.printing)
        #except True:
        #    return False
        #else:
        #    return True

    def test_add_print_job(self, print_job):
        self.queue_printer = []
        self.queue_printer.append(print_job)
        self.assertNotEqual(self.queue_printer, [])

    def test_print_job_error(self):
        self.queue_printer = []
        self.error_flag = True
        self.error_description = "nothing to print"
        self.assertEqual(self.queue_printer, [])
        
        self.assertTrue(self.error_flag)
        self.assertEqual(self.error_description, "nothing to print")

    def test_print_job(self):
        self.printing = True
        self.queue_printer = []
        self.queue_printer.pop(0)

        self.assertTrue(self.printing)
        self.assertNotEqual(self.queue_printer, 0)



    def test_reset_printer(self):
        self.printing = False
        self.error_flag = False
        self.error_description = ""

        self.assertFalse(self.printing)
        self.assertFalse(self.error_flag)
        self.assertEqual(self.error_description, "")


    

if __name__ == '__main__':
  unittest.main()