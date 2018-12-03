import re


rectangle_regex = \
    r'(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)'


class Rectangle:
    def __init__(self, _id, left, top, width, height):
        self.id = _id
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self._coords = None

    @property
    def coords(self):
        if not self._coords:
            self._coords = {
                (i, j)
                for i in range(self.top, self.top + self.height)
                for j in range(self.left, self.left + self.width)
            }

        return self._coords


def parse_rectangle(rectangle_string):
    return Rectangle(
        *map(
            int,
            re.search(
                rectangle_regex,
                rectangle_string
            ).group('id', 'left', 'top', 'width', 'height')
        )
    )


def read_input():
    with open('input-3') as input_file:
        return map(parse_rectangle, input_file.read().strip().split('\n'))


def generate_coords(rectangle):
    for i in range(rectangle.top, rectangle.top + rectangle.height):
        for j in range(rectangle.left, rectangle.left + rectangle.width):
            yield (i, j)
