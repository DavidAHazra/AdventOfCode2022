import collections


class CPU:
    def __init__(self):
        self.queue = collections.deque([])
        self.current_time = 0
        self.x = 1
        self.x_history = {0: 1}
        self.executing = None

    def add_x(self, amount):
        self.queue.append(amount)

    def noop(self):
        self.queue.append("noop")

    def tick(self):
        # Start of cycle
        self.current_time += 1
        self.x_history[self.current_time] = self.x

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

    crt_output, current_row = [], []
    for pixel in range(1, 240):
        sprite_start = cpu.x_history[pixel]
        pixel %= 40

        current_row.append('#' if sprite_start <= pixel < sprite_start + 3 else ' ')

        if len(current_row) == 40:
            print("".join(current_row))
            crt_output.append(current_row)
            current_row = []

    print("".join(current_row))
