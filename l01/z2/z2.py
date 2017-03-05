import unicodedata
from collections import defaultdict
from pprint import pprint

DEFAULT_NAME = ''
LETTER_PREFIX = 'L'
NAME_FILTERS = ['cyrillic', 'greek']

# http://vietunicode.sourceforge.net/charset/
VIETNAMESE_RANGES = [
    range(0x0000, 0x007F + 1),  # basic latin
    range(0x0080, 0x00FF + 1),  # latin-1 supplement
    range(0x0100, 0x024F + 1),  # latin extended A and B
    range(0x1E00, 0x1EFF + 1),  # Latin Extended Additional
    range(0x0300, 0x036F + 1),  # Combining Diacritical Marks
    range(0x20AB, 0X20AB + 1)   # Dong currency symbol
]

# http://www.fileformat.info/info/unicode/block/index.htm
CJK_RANGES = [
    range(0x4E00, 0x9FFF + 1),
    range(0x2E80, 0x2EFF + 1),
    range(0x3000, 0x303F + 1),
    range(0x31C0, 0x31EF + 1),
    range(0x3200, 0x32FF + 1),
    range(0x3300, 0x33FF + 1),
    range(0x3400, 0x4DBF + 1),
    range(0xF900, 0xFAFF + 1),
    range(0xFE30, 0xFE4F + 1),
    range(0x20000, 0x2A6DF + 1),
    range(0x2A700, 0x2B73F + 1),
    range(0x2B740, 0x2B81F + 1),
    range(0x2B820, 0x2CEAF + 1),
    range(0x2F800, 0x2FA1F + 1)
]

RANGES = {
    'vietnamese': VIETNAMESE_RANGES,
    'braille': [range(0x2800, 0x28FF + 1)],
    'arabic': [range(0x0600, 0x06FF + 1)],
    'cjk': CJK_RANGES
}

def get_specific_category(character_number):
    for category_name, ranges in RANGES.items():
        for unicode_range in ranges:
            if character_number in unicode_range:
                return category_name

    return None

with open('znaki_wikipedii.txt') as f:
    lines = f.readlines()

categories = defaultdict(lambda: set())

for line in lines:
    for character in line:
        category = unicodedata.category(character)
        character_name = unicodedata.name(character, DEFAULT_NAME).lower()
        character_number = ord(character)

        specific_category = get_specific_category(character_number)
        if specific_category:
            categories[specific_category].add(character)
            if specific_category != 'vietnamese':
                continue

        if category[0] == LETTER_PREFIX:
            for name in NAME_FILTERS:
                if name in character_name:
                    category += ' ' + name

        categories[category].add(character)

for category in sorted(categories):
    pprint('{}: {}'.format(category, ' '.join(sorted(categories[category]))), width=80)
