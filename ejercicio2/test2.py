import unittest
from ejr2 import determinante_iterativo, determinante_recursivo

class Test2(unittest.TestCase):
    def setUp(cls):
        cls.matriz = [[1,2,3],[1,2,3],[1,2,3]]
        cls.matriz2 = [[4,-1,3],[2,-1,4],[1,2,3]]
    
    def test1(self):
        self.assertEqual(determinante_iterativo(self.matriz), 0)
    def test2(self):
        self.assertEqual(determinante_iterativo(self.matriz2),-27)
    def test3(self):
        self.assertEqual(determinante_recursivo(self.matriz, 0, 0), '0')
    def test4(self):
        self.assertEqual(determinante_recursivo(self.matriz2, 0, 0), '-27')

if __name__ == '__main__':
    unittest.main()