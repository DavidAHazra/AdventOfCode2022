import sympy


def get_equation(action):
    if action.isnumeric() or action == "????":
        return action

    left, op, right = action[:4], action[5], action[7:]

    left_eq = get_equation(monkey_shouts[left])
    right_eq = get_equation(monkey_shouts[right])
    combined = f"{left_eq} {op} {right_eq}"
    if op == "=":
        return combined

    return f"({combined})"


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
        monkey_shouts = {
            line.strip().split(":")[0].strip(): line.strip().split(":")[1].strip()
            for line in input_file
        }

    monkey_shouts["humn"] = "????"

    # There can't be any cycles in the graph, so run DFS to find the full equation for root
    root_equation = get_equation(f"{monkey_shouts['root'][:4]} = {monkey_shouts['root'][7:]}")
    left_side, right_side = root_equation.replace("????", "x").split("=")
    right_side = int(eval(right_side))

    print("Solve this equation for x:")
    print("Left side:", left_side)
    print("Right side:", right_side)

    # Solve for x :)
    human_shout = int(sympy.solve(sympy.sympify(f"Eq({left_side}, {right_side})"))[0])
    print(f"\nYou must shout {human_shout} in order to pass root's equality test.")
