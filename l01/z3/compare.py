SEPARATOR = '-------------------------------------------------'

total = 0
different = 0


def print_diff(reference, actual):
    print(reference, end='')
    print(actual, end='')
    print(SEPARATOR)


with open('tokenized_quotes.txt') as nltk_quotes:
    with open('out.txt') as my_quotes:
        for reference in nltk_quotes:
            total += 1
            mine = my_quotes.readline()
            if reference != mine:
                different += 1
                print_diff(reference, mine)

print('Different lines:', different)
print('Total number of lines: ', total)

