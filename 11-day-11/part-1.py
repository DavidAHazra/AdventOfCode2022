import collections
import heapq
import math


class Monkey:
    def __init__(self, items, operation, test_div, eval_true_monkey, eval_false_monkey):
        self.items = collections.deque(items)
        self.operation = operation
        self.test_div = test_div
        self.eval_true_monkey = eval_true_monkey
        self.eval_false_monkey = eval_false_monkey

        self.num_inspects = 0

    def get_throws(self):
        throws = collections.defaultdict(list)
        while self.items:
            item = self.items.popleft()
            self.num_inspects += 1

            worry_level = eval(self.operation.replace("old", f"{item}")) // 3
            condition = worry_level % self.test_div == 0
            throws[self.eval_true_monkey if condition else self.eval_false_monkey].append(worry_level)

        return throws


def simulate_round(monkey_dict):
    for monkey_number in monkey_dict.keys():
        monkey_throws = monkey_dict[monkey_number].get_throws()

        for to_monkey in monkey_throws:
            monkey_dict[to_monkey].items.extend(monkey_throws[to_monkey])


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [line.strip() for line in input_file]

    monkeys = dict()
    for index in range(0, len(lines), 7):
        monkeys[int(lines[index][-2])] = Monkey(
            [int(item) for item in lines[index + 1].replace("Starting items: ", "").replace(',', '').split()],
            lines[index + 2].replace("Operation: new = ", ""),
            int(lines[index + 3].replace("Test: divisible by ", "")),
            int(lines[index + 4][-1]),
            int(lines[index + 5][-1])
        )

    for _ in range(20):
        simulate_round(monkeys)

    monkey_business = math.prod(heapq.nlargest(2, [monkeys[i].num_inspects for i in monkeys]))
    print(f"The level of monkey business after 20 rounds is {monkey_business}.")
