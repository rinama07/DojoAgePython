class FindShorterWord:

    @staticmethod
    def find_shorter_word(words):

        words_quantity = int(words.__len__())
        shorter = ""

        for index in range(words_quantity):
            word = words[index]

            if index == 0 or word.__len__() < shorter.__len__():
                shorter = word

        return shorter
