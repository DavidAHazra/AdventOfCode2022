import collections


class CPU:
    def __init__(self):
        self.queue = collections.deque([])
        self.current_time = 0
        self.x = 1
        self.signal = {}
        self.executing = None

    def add_x(self, amount):
        self.queue.append(amount)

    def noop(self):
        self.queue.append("noop")

    def tick(self):
        # Start of cycle
        self.current_time += 1
        self.signal[self.current_time] = self.current_time * self.x

        if self.queue:
            if self.executing is None:
                current = self.queue.popleft()
                self.executing = [
                    0 if current == "noop" else current,
                    0 if current == "noop" else 1
                ]

            else:
                self.executing[1] -= 1

        # End of cycle
        if self.executing[1] == 0:
            self.x += self.executing[0]
            self.executing = None


if __name__ == '__main__':
    cpu = CPU()

    with open("input.txt", 'r') as input_file:
        for line in input_file:
            command = line.split()

            if command[0] == "addx":
                cpu.add_x(int(command[1]))

            else:
                cpu.noop()

    while cpu.queue:
        cpu.tick()

    signal_sum = sum(cpu.signal[cycle] for cycle in [20, 60, 100, 140, 180, 220])
    print(f"The sum of the signal strength at the specified cycles is {signal_sum}.")
