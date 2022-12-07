import bisect


class Node:
    def __init__(self, parent, dir_name=None):
        self.parent = parent
        self.dir_name = dir_name
        self.value = 0
        self.children = dict()


def combine_post_order(current_node):
    if current_node:
        for child_path in current_node.children:
            combine_post_order(current_node.children[child_path])

        current_node.parent.value += current_node.value


if __name__ == '__main__':
    sentinel = Node(None)
    current = sentinel

    # Parse input into node tree
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            command = line.split()

            if command[0] == '$':
                if command[1] == 'cd':
                    name = command[2]

                    if name == "..":
                        current = current.parent

                    elif name in current.children:
                        current = current.children[name]

                    else:
                        new_dir = Node(current, name)
                        current.children[name] = new_dir
                        current = new_dir

            elif command[0] != 'dir':
                value, file = command
                current.value += int(value)

    # Extract root of tree structure and combine child values into parents
    root = sentinel.children['/']
    combine_post_order(root)

    # Insertion sort values into sorted list
    stack, sorted_sizes = [root], []
    while stack:
        current = stack.pop()
        bisect.insort(sorted_sizes, current.value)

        for adj in current.children:
            stack.append(current.children[adj])

    # Calculate the minimum amount of space needed to delete
    unused_space = 70000000 - root.value
    to_delete = 30000000 - unused_space

    # Binary search the closest value greater than to_delete
    deletion_index = bisect.bisect_left(sorted_sizes, to_delete)
    print(f"To have enough unused space, you need to delete the directory of size {sorted_sizes[deletion_index]}.")


