"""
Você está resolvendo este problema.
Este problema foi utilizado em 181 Dojo(s).
Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número,
em seguida você faz a soma desses resultados.
A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma.
Se ao repetir o procedimento diversas vezes obtivermos o valor 1,
o número inicial é considerado feliz.
Tomamos o 7, que é um número feliz:
7² = 49
4² + 9² = 97
9² + 7² = 130
1² + 3² + 0² = 10
1² + 0² = 1
Podemos observar nesse exemplo que os números 49, 97, 130 e 10 também são felizes.
Existem infinitos números felizes.
E um número triste? Como sabemos que um número não será feliz?
Desenvolva um programa que determine se um número é feliz ou triste.
"""


class HappyNumber:

    used_numbers = []
    happy_number = 1

    def is_happy_number(self, number):
        total_sum = self.power_and_sum_each_number(number)
        if total_sum == self.happy_number:
            return True

        if self.is_number_already_used(total_sum):
            return False

        return self.is_happy_number(total_sum)

    def is_number_already_used(self, number):
        if self.used_numbers.__contains__(number):
            return True

        self.used_numbers.append(number)
        return False

    @staticmethod
    def power_and_sum_each_number(number):
        total_sum = 0

        while number:
            total_sum += pow(number % 10, 2)  # number % 10 = digit of the number
            number //= 10

        return total_sum
