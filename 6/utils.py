def read_input():
    with open('input-6') as input_file:
        return [
            (int(x), int(y))
            for x, y in [
                line.split(', ')
                for line in input_file.read().strip().split('\n')
            ]
        ]


def dist(p, q):
    return sum(abs(_p - _q) for _p, _q in zip(p, q))


def get_extrema(coords):
    return (
        min(x for x, y in coords),
        min(y for x, y in coords),
        max(x for x, y in coords),
        max(y for x, y in coords)
    )

def get_closest(point, coords):
    point_dists = {p: dist(point, p) for p in coords}
    closest_point, _dist = min(point_dists.items(), key=lambda p: p[1])
    if list(point_dists.values()).count(_dist) == 1:
        return closest_point
