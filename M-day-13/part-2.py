import ast
import itertools
from functools import cmp_to_key


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


def compare_ternary(left, right):
    return {True: 1, None: 0, False: -1}[compare(left, right)]


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [[[2]], [[6]]] + [ast.literal_eval(line.strip()) for line in input_file if line != '\n']

    two_loc, six_loc = -1, -1
    for index, line in enumerate(sorted(lines, reverse=True, key=cmp_to_key(compare_ternary))):
        two_loc = index + 1 if line == [[2]] else two_loc
        six_loc = index + 1 if line == [[6]] else six_loc

    print(f"The decoder key is {two_loc * six_loc}.")
