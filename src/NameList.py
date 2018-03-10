class NameList:

    @staticmethod
    def name_list(names):
        names_quantity = int(names.__len__())
        index_of_diff_char = names_quantity - 1
        final_string = ""

        for index in range(names_quantity):
            name = names[index].get('name')
            glue_char = ","

            if index == index_of_diff_char:
                glue_char = " &"

            if index > 0:
                name = "{} {}".format(glue_char, name)

            final_string += name

        return final_string
