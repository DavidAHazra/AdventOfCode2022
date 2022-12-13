import ast
import itertools


def compare(left, right):
    for left_item, right_item in itertools.zip_longest(left, right):
        if left_item is None:
            return True

        if right_item is None:
            return False

        if type(left_item) is int and type(right_item) is int:
            if left_item > right_item:
                return False

            if left_item < right_item:
                return True

        elif type(left_item) is list and type(right_item) is list:
            state = compare(left_item, right_item)

            if type(state) is bool:
                return state

        elif type(left_item) is int and type(right_item) is list:
            state = compare([left_item], right_item)

            if type(state) is bool:
                return state

        elif type(right_item) is int and type(left_item) is list:
            state = compare(left_item, [right_item])

            if type(state) is bool:
                return state


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [line.strip() for line in input_file]

    pairs = [
        (ast.literal_eval(lines[i]), ast.literal_eval(lines[i + 1]))
        for i in range(0, len(lines), 3)
    ]

    index_sum = sum(index + 1 for index, (left, right) in enumerate(pairs) if compare(left, right))
    print(f"The sum of the indices of pairs in the right order is {index_sum}.")