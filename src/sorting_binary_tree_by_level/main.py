
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def append_level(node, level_value_dict, actual_level):
    actual_level += 1

    if node.left:
        level_value_dict.setdefault(str(actual_level), []).append(node.left.value)

    if node.right:
        level_value_dict.setdefault(str(actual_level), []).append(node.right.value)

    if node.left:
        append_level(node.left, level_value_dict, actual_level)

    if node.right:
        append_level(node.right, level_value_dict,actual_level)

def tree_by_levels(node):
    if node is None:
        return []

    value_dict = {}
    actual_level = 0

    value_dict.setdefault(str(actual_level), []).append(node.value)
    append_level(node, value_dict, actual_level)

    value_list = []
    for _, values in value_dict.items():
        value_list.extend(values)

    return value_list


if __name__ == '__main__':
    print(tree_by_levels(None))
    print(tree_by_levels(Node(Node(None, Node(Node(None, None, 7), None, 4), 2), Node(Node(None, None, 5), Node(Node(None, None, 8), None, 6), 3), 1)))

'''
            1
    2               3
4               5       6
7               8
'''