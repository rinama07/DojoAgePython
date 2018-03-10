"""
Dado uma letra ('A' a 'Z'), exiba um diamante iniciando em 'A' e tendo a letra fornecida com o ponto mais distante.
Por exemplo, dado a letra 'E' temos:
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
 *
Dado a letra 'C' temos:
  A
 B B
C   C
 B B
  A
"""
from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class Diamond:

    left_space = 0
    space_between_letters = 0
    first_letter = True

    def diamond_generator(self, letter):
        letters = xrange(ord('A'), ord(letter)+1)
        lines = ["" for _ in range(len(letters) * 2 - 1)]
        first_position = 0
        last_position = len(lines) - 1

        self.left_space = len(letters)
        self.space_between_letters = 1

        for letter in letters:
            line = self.generate_line(letter)
            lines[first_position] = line
            lines[last_position] = line
            first_position += 1
            last_position -= 1

        return lines

    def generate_line(self, letter):
        line = self.repeat_space(self.left_space) + chr(letter)

        if self.first_letter:
            self.first_letter = False
        else:
            line += self.repeat_space(self.space_between_letters) + chr(letter)
            self.space_between_letters += 2

        self.left_space -= 1

        return line

    @staticmethod
    def repeat_space(t):
        spaces = ""
        for i in range(t):
            spaces += " "
        return spaces
