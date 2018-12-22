from utils import parse_to_tree, read_input


def get_metadata_sum(node):
    return sum(node.metadata) + sum(map(get_metadata_sum, node.children))


if __name__ == '__main__':
    tree = parse_to_tree(read_input())
    print(get_metadata_sum(tree))
