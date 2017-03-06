import re

BLACKLIST = ['szablon', 'uwagi', 'kategoria' 'wikipedia', 'imieniny', 'wydarzenia w', 'strona ujednoznaczniająca',
             'lata', 'mapy i zdjęcia', 'gmina', 'liga', 'świata', 'igrzyska', 'pułk', 'brygada', 'award', 'fryderyki',
             'oscar', 'parafia', 'ulica', 'mistrzostwa', 'wikiprojekt', 'prowincja', ':', 'nagroda', 'batalion',
             'wybory', 'wiek']
BOLDED = re.compile("'''([^'].*?)'''")


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

    result.update(BOLDED.findall(paragraph))
    result = set(map(str.lower, (map(str.strip, result))))

    s = ' # '.join(result)
    for word in BLACKLIST:
        if word in s:
            return set()

    to_split = []
    for word in result:
        if ', ' in word:
            to_split.append(word)

    for word in to_split:
        result.remove(word)
        result.update(word.split(', '))

    return result


if __name__ == '__main__':
    with open('poczatki_wikipediowe.txt') as f:
        header = f.readline()
        while header:
            paragraph = f.readline()
            separator = f.readline()
            if separator == '\n':
                synonyms = get_synonyms(header, paragraph)
                if len(synonyms) > 1:
                    print(' # '.join(synonyms).replace('&amp;', '&'))
            header = f.readline()

            while header and not header.startswith('### '):
                header = f.readline()
