import unicodedata


def tokenize(line):
    result = []
    for word in line.lower().split():
        if not word:
            continue

        while word and unicodedata.category(word[0])[0] == 'P':
            result.append(word[0])
            word = word[1:]

        suffix = []
        while word and unicodedata.category(word[-1])[0] == 'P':
            suffix.append(word[-1])
            word = word[:-1]

        word and result.append(word)
        result.extend(suffix[::-1])

    return result


with open('cytaty.txt') as quotes:
    for quote in quotes:
        print(' '.join(tokenize(quote[2:])))
