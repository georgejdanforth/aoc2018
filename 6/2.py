from utils import dist, get_extrema, read_input

if __name__ == '__main__':
    coords = read_input()
    min_x, min_y, max_x, max_y = get_extrema(coords)

    AROUND = 1

    size = 0

    for x in range(min_x - AROUND, max_x + AROUND):
        for y in range(min_y - AROUND, max_y + AROUND):
            if sum(dist((x, y), pair) for pair in coords) < 10000:
                size += 1

    print(size)
