def count_lines(name):
    with open(name, 'r') as example_file:
        count = len(example_file.readlines())
    return count


def count_chars(name):
    example_file = open(name, 'r')
    count = len(example_file.read())
    example_file.close()
    return count


def test(name):
    line_count = count_lines(name)
    char_count = count_chars(name)
    return line_count, char_count


# print('Modul is imported successfully')

if __name__ == '__main__':
    pass
