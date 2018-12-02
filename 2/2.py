from itertools import combinations


def read_input():
    with open('input-2') as input_file:
        return input_file.read().strip().split('\n')

def is_match(a, b):
    misses = 0
    for _a, _b in zip(a, b):
        misses += _a != _b
        if misses > 1:
            return False

    return misses == 1


def find_match(words):
    for a, b in combinations(sorted(words), 2):
        if is_match(a, b):
            return a, b


def get_similar_letters(a, b):
    return ''.join(set(a) & set(b))


if __name__ == '__main__':
    print(get_similar_letters(*find_match(read_input())))
