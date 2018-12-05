import re

from utils import read_input, annihilate


def generate_regexes():
    return [r'[{}{}]'.format(chr(i), chr(i + 32)) for i in range(65, 91)]


def shortest_length(polymer):
    return sorted([
        len(annihilate(re.sub(regex, '', polymer)))
        for regex in generate_regexes()
    ])[0]


if __name__ == '__main__':
    print(shortest_length(read_input()))
