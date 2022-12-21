def eval_operation(statement, monkey_values):
    left_name, right_name = statement[:4], statement[7:]

    if left_name in monkey_values and right_name in monkey_values:
        return {
            "+": monkey_values[left_name] + monkey_values[right_name],
            '-': monkey_values[left_name] - monkey_values[right_name],
            '*': monkey_values[left_name] * monkey_values[right_name],
            "/": monkey_values[left_name] / monkey_values[right_name]
        }[statement[5]]


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [line.strip().split(":") for line in input_file]

    # Separate monkeys based on known shout value
    numbers, statements = dict(), dict()
    for name, action in lines:
        action = action.strip()

        if action.isnumeric():
            numbers[name] = int(action)

        else:
            statements[name] = action

    # Loop until root's value is known
    while statements and "root" not in numbers:
        set_number_monkey = []
        for name in statements:
            converted = eval_operation(statements[name], numbers)

            if converted is not None:
                set_number_monkey.append((name, converted))

        # We know the value for these monkeys
        for name, number in set_number_monkey:
            del statements[name]
            numbers[name] = number

    print(f"The value shouted by the monkey 'root' is {int(numbers['root'])}.")
