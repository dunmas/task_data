def parse_cook_book(data):
    with open(data, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = make_dict(lines)

        return result


def make_dict(lines):
    result = dict()
    buff_list = []

    for line in lines:
        if line != '\n':
            buff_list.append(line)
        else:
            result[buff_list[0][:-1]] = make_ingredient(buff_list[2:])

            buff_list.clear()

    return result


def make_ingredient(raw_list):
    result = []
    for line in raw_list:
        elements = line[:-1].split(' | ')
        result.append({'ingredient_name': elements[0], 'quantity': elements[1], 'measure': elements[2]})

    return result


data = 'data.txt'

print(parse_cook_book(data))
