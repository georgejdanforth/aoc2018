from utils import parse_to_tree, read_input


def get_children(children, *indices):
    return [children[i - 1] for i in indices if 1 <= i <= len(children)]

def get_value(node):
    if node.num_children == 0:
        return sum(node.metadata)
    else:
        return sum(map(get_value, get_children(node.children, *node.metadata)))


if __name__ == '__main__':
    tree = parse_to_tree(read_input())
    print(get_value(tree))
