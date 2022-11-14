def parse_cook_book(data):
    with open(data, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = make_dict(lines)

        return result

def make_dict(lines):
    result = dict()

    for line in lines:
        buff_list = []

        if line != '\n':
            buff_list.append(line)
        else:
            result[buff_list[0][:-2]] = make_ingredient(buff_list[1:])

            buff_list.clear()


def make_ingredient(raw_list):
    pass

data = 'data.txt'

parse_cook_book(data)