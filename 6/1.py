from utils import get_closest, get_extrema, read_input


if __name__ == '__main__':
    coords = read_input()
    min_x, min_y, max_x, max_y = get_extrema(coords)

    AROUND = 1

    edges = set()

    for x in range(min_x - AROUND, max_x + AROUND):
        edges.add(get_closest((x, min_y - AROUND), coords))
        edges.add(get_closest((x, max_y + AROUND), coords))

    for y in range(min_y - AROUND, max_y + AROUND):
        edges.add(get_closest((min_x - AROUND, y), coords))
        edges.add(get_closest((max_x + AROUND, y), coords))

    counts = {pair: 0 for pair in coords if pair not in edges}
    for x in range(min_x - AROUND, max_x + AROUND):
        for y in range(min_y - AROUND, max_y + AROUND):
            closest = get_closest((x, y), coords)
            if closest not in edges:
                counts[closest] += 1

    print(max(counts.values()))
