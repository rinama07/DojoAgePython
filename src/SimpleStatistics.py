# Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:
#
#     Valor mínimo
#     Valor máximo
#     Número de elementos na seqüência
#     Valor médio
#
# Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:
#
#     Valor mínimo: -2
#     Valor máximo: 92
#     Número de elementos na seqüência: 6
#     Valor médio: 18.1666666
import math
from statistics import mean


class SimpleStatistics:

    def get_lista_numeros_a_partir_de_string(self, numeros_em_string):
        lista_numeros = numeros_em_string.split(",")
        return list(map(int, lista_numeros))

    def get_menor_valor_da_lista(self, numeros):
        return min(numeros)

    def get_maior_valor_da_lista(self, numeros):
        return max(numeros)

    def get_quantidade_itens_da_lista(self, numeros):
        return len(numeros)

    def get_media_itens_da_lista(self, numeros):
        return mean(numeros)
