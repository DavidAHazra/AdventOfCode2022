from collections import deque


if __name__ == '__main__':
    is_stack_input = True
    stacks = []

    with open("input.txt", 'r') as input_file:
        for line in input_file:
            if line == '\n':
                is_stack_input = False
                continue

            if is_stack_input:
                for column in range(1, len(line), 4):
                    stack_index = (column - 1) // 4
                    if len(stacks) <= stack_index:
                        stacks.append(deque())

                    if line[column].isalpha():
                        stacks[stack_index].appendleft(line[column])

            else:
                details = line.strip().replace("move", '').replace("from", '').replace("to", '').strip().split(' ')
                count, from_stack, to_stack = [int(detail) for detail in details if detail != '']

                for _ in range(count):
                    stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

    top_crates = "".join(stack[-1] for stack in stacks)
    print(f"After reorganising the crates, the crates at the top of each stack are: {top_crates}.")
