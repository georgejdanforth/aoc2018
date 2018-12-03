from utils import generate_coords, read_input


def collect_overlaps(rectangles):
    counter = {}
    for rectangle in rectangles:
        for coords in generate_coords(rectangle):
            if coords in counter:
                counter[coords] += 1
            else:
                counter[coords] = 1

    return sum([count > 1 for count in counter.values()])


if __name__ == '__main__':
    print(collect_overlaps(read_input()))
