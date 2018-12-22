from dataclasses import dataclass


@dataclass
class Node:
    num_children: int
    num_metadata_entries: int
    children: list
    metadata: list

    def __repr__(self):
        return f'<Node {self.num_children} | {self.num_metadata_entries}>'

    def print_tree(self, depth=0):
        print(('\t' * depth) + repr(self))
        for child in self.children:
            child.print_tree(depth + 1)


def read_input():
    with open('input-8') as input_file:
        return [int(i) for i in input_file.read().strip().split(' ')]


def _parse_to_tree(nums):
    num_children, num_metadata_entries, *rest = nums
    children = []
    for _ in range(num_children):
        child, rest = _parse_to_tree(rest)
        children.append(child)

    return (
        Node(
            num_children,
            num_metadata_entries,
            children,
            rest[:num_metadata_entries]
        ),
        rest[num_metadata_entries:]
    )


def parse_to_tree(nums):
    return _parse_to_tree(nums)[0]
