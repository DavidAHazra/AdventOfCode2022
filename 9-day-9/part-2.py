import numpy as np

ADJACENT = {(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}

CARDINALS = {
    'R': np.array([0, 1]),
    'L': np.array([0, -1]),
    'U': np.array([1, 0]),
    'D': np.array([-1, 0])
}


class LongRope:
    def __init__(self, num_knots):
        self.knots = [np.array([0, 0]) for _ in range(num_knots)]
        self.unique_tail = set()

    def move(self, movement):
        self.knots[0] += CARDINALS[movement]

        for i in range(len(self.knots) - 1):
            displacement = self.knots[i] - self.knots[i + 1]

            if tuple(displacement) not in ADJACENT:
                self.knots[i + 1] += np.sign(displacement)

        self.unique_tail.add(tuple(self.knots[-1]))


if __name__ == '__main__':
    rope = LongRope(10)

    with open("input.txt", 'r') as input_file:
        for line in input_file:
            direction, amount = line.strip().split()
            for _ in range(int(amount)):
                rope.move(direction)

    print(f"The tail of the rope moves to {len(rope.unique_tail)} unique positions.")
