
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
        result = {}

        for dish in dishes:
            for ingred in self.cook_book[dish]:
                if ingred['ingredient_name'] not in result:
                    result[ingred['ingredient_name']] = {'measure': ingred['measure'],
                                                         'quantity': int(ingred['quantity']) * person_count}
                else:
                    result[ingred['ingredient_name']]['quantity'] += int(ingred['quantity']) * person_count

        return result

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

# task 3


def file_processing(files: list):
    pre_dict = {}
    result_file = 'result.txt'

    # создаём соответствие "файл - количество строк"
    for file in files:
        pre_dict[file] = sum(1 for line in open(file, 'r', encoding='utf-8'))

    buffer = ""

    for file in sorted(pre_dict, key=pre_dict.get):
        buffer += f"{file}\n" \
                  f"{pre_dict[file]}\n" \

        with open(file, 'r', encoding='utf-8') as data:
            for line in data.readlines():
                buffer += line
            buffer += '\n'

    with open(result_file, 'w', encoding='utf-8') as result:
        result.write(buffer)


data = 'data.txt'
cook = CookBook(data)
files = ['1.txt', '2.txt']

file_processing(files)

print(cook.cook_book)

print(cook.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
