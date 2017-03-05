import re

ciapki = re.compile("'''([^'].*?)'''")


def get_synonyms(header, paragraph):
    result = set()

    try:
        header = header[:header.index('(') - 1]
        result.add(header[4:])
    except:
        result.add(header[4:-1])


    try:
        paragraph = paragraph[:paragraph.index('(')]
    except:
        pass

    result.update(ciapki.findall(paragraph))
    return set(map(str.strip, map(str.lower, result)))


if __name__ == '__main__':
    with open('poczatki_wikipediowe.txt') as f:
        header = f.readline()
        while header:
            paragraph = f.readline()
            separator = f.readline()
            if separator == '\n':
                synonyms = get_synonyms(header, paragraph)
                if len(synonyms) > 1:
                    print(' # '.join(synonyms))
            header = f.readline()

            while header and not header.startswith('### '):
                header = f.readline()
