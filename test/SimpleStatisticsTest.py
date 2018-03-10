import unittest
from src.SimpleStatistics import SimpleStatistics


class SimpleStatisticsTest(unittest.TestCase):

    def test_deve_retornar_menor_numero(self):
        valor_esperado = -2
        lista_numeros = [6, 9, 15, -2, 92, 11]
        valor_retornado = SimpleStatistics().get_menor_valor_da_lista(lista_numeros)

        self.assertEqual(valor_esperado, valor_retornado)

    def test_deve_retornar_maior_numero(self):
        valor_esperado = 92
        lista_numeros = [6, 9, 15, -2, 92, 11]
        valor_retornado = SimpleStatistics().get_maior_valor_da_lista(lista_numeros)

        self.assertEqual(valor_esperado, valor_retornado)

    def test_deve_retornar_quantidade_numeros_inseridos(self):
        valor_esperado = 6
        lista_numeros = [6, 9, 15, -2, 92, 11]
        valor_retornado = SimpleStatistics().get_quantidade_itens_da_lista(lista_numeros)

        self.assertEqual(valor_esperado, valor_retornado)

    def test_deve_retornar_valor_medio(self):
        valor_esperado = 5
        lista_numeros = [5, 5, 5, 5, 5, 5]
        valor_retornado = SimpleStatistics().get_media_itens_da_lista(lista_numeros)

        self.assertEqual(valor_esperado, valor_retornado)

    def test_deve_retornar_array_inteiros(self):
        valor_esperado = [6, 9, 15, -2, 92, 11]
        string = "6, 9, 15, -2, 92, 11"
        valor_retornado = SimpleStatistics().get_lista_numeros_a_partir_de_string(string)

        self.assertEqual(valor_esperado, valor_retornado)


if __name__ == '__main__':
    unittest.main()
