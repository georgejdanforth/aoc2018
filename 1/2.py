from itertools import cycle, accumulate


def read_input():
    with open('input-1') as input_file:
        return map(int, input_file.read().strip().split('\n'))


def find_repeated_freq(changes):
    freqs = set()
    for current_freq in accumulate(cycle(changes)):
        if current_freq in freqs:
            return current_freq

        freqs.add(current_freq)


if __name__ == '__main__':
    print(find_repeated_freq(read_input()))

