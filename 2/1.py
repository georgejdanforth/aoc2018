from collections import Counter


def read_input():
    with open('input-2') as input_file:
        return input_file.read().strip().split('\n')


def get_repeats(word):
    freq_occurrences = set(Counter(word).values())
    return 2 in freq_occurrences, 3 in freq_occurrences


def get_checksum(words):
    twos, threes = 0, 0
    for word in words:
        _twos, _threes = get_repeats(word)
        twos += _twos
        threes += _threes

    return twos * threes


if __name__ == '__main__':
    print(get_checksum(read_input()))
