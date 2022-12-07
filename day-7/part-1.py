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

    # DFS traversal of the tree to iterate over nodes
    stack, size_sum = [root], 0
    while stack:
        current = stack.pop()
        if current.value <= 100000:
            size_sum += current.value

        for adj in current.children:
            stack.append(current.children[adj])

    print(f"The sum of the sizes of all directories with size at most 100000 is: {size_sum}.")
