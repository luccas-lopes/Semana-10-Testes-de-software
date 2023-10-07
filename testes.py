import unittest
import numeroromano as nr


class numerosRomanosTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.numerosromanos = []

        self.numerosromanos.append('I')
        self.numerosromanos.append('V')
        self.numerosromanos.append('II')
        self.numerosromanos.append('XXII')
        self.numerosromanos.append('IX')
        self.numerosromanos.append('XXIV')

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testI(self):
        self.assertEqual(1, nr.converte(self.numerosromanos[0]))

    def testV(self):
        self.assertEqual(5, nr.converte(self.numerosromanos[1]))

    def testII(self):
        self.assertEqual(2, nr.converte(self.numerosromanos[2]))

    def testXXII(self):
        self.assertEqual(22, nr.converte(self.numerosromanos[3]))

    def testIX(self):
        self.assertEqual(9, nr.converte(self.numerosromanos[4]))

    def testXXIV(self):
        self.assertEqual(24, nr.converte(self.numerosromanos[5]))


if __name__ == "__main__":
    unittest.main()
