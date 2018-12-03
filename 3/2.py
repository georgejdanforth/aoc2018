from utils import generate_coords, read_input


def find_non_overlapping_rectangle(rectangles):
    for a in rectangles:
        overlaps = False
        for b in rectangles:
            if a.id == b.id:
                continue
            if a.coords & b.coords:
                overlaps = True
                break

        if not overlaps:
            return a.id


if __name__ == '__main__':
    print(find_non_overlapping_rectangle(list(read_input())))
