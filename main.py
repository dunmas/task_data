
class CookBook:
    @staticmethod
    def _make_ingredients(raw_list):
        result = []

        for line in raw_list:
            elements = line[:-1].split(' | ')
            result.append({'ingredient_name': elements[0], 'quantity': elements[1], 'measure': elements[2]})

        return result

    def __init__(self, data_file):
        self.file = data_file
        self.cook_book = self._parse_cook_book(data_file)

    def get_shop_list_by_dishes(self, dishes, person_count):
        pass

    def _parse_cook_book(self, data_file):
        with open(data_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            result = self._make_cook_book_dict(lines)

            return result

    def _make_cook_book_dict(self, lines):
        result = dict()
        buff_list = []

        for line in lines:
            if line != '\n':
                buff_list.append(line)
            else:
                result[buff_list[0][:-1]] = self._make_ingredients(buff_list[2:])
                buff_list.clear()

        return result


data = 'data.txt'
cook = CookBook(data)

print(cook.cook_book)
