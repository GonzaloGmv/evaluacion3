import unittest
import csv
from ejr3 import info, mas_pasajeros, mas_tripulacion, pasajeros, at, ordenar

class Test3(unittest.TestCase):
    @classmethod
    def setUp(self):
        filas = []
        with open('naves.csv', 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                if i[0] == 'Nombre':
                    keys = i
                    del i
                else:
                    filas.append(i)
        self.keys = keys
        self.filas = filas
    def test1(self):
        self.assertEqual(info("Halcon Milenario", self.keys, self.filas), ['Halcon Milenario', '34.37', '3', '4'])
    def test1_2(self):
        self.assertEqual(info("Estrella de la Muerte", self.keys, self.filas), ['Estrella de la Muerte', '105', '5', '1500'])
    def test2(self):
        self.assertEqual(mas_pasajeros(self.keys, self.filas), ['Ala X', 'Caza TIE', 'Destructor estelar', 'Lanzadera imperial', 'Estrella de la Muerte'])
    def test3(self):
        self.assertEqual(mas_tripulacion(self.keys, self.filas), 'Destructor estelar')
    def test4(self):
        self.assertEqual(at(self.filas), 'AT-AT')
    def test5(self):
        self.assertEqual(pasajeros(self.keys, self.filas), ['Ala X', 'Caza TIE', 'Destructor estelar', 'Lanzadera imperial', 'Estrella de la Muerte', 'AT-AT'])
    def test6(self):
        self.assertEqual(ordenar(self.keys, self.filas), ['Caza TIE', '20.1', '2', '21']
                                                        ['AT-AT', '27', '8', '13']
                                                        ['Ala X', '31', '1', '17']
                                                        ['Halcon Milenario', '34.37', '3', '4']
                                                        ['Destructor estelar', '74', '12', '1000']
                                                        ['Lanzadera imperial', '80', '6', '2000']
                                                        ['Estrella de la Muerte', '105', '5', '1500'])
if __name__ == '__main__':
    unittest.main()