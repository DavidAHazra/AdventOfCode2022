import numpy as np

ADJACENT = {(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}

CARDINALS = {
    'R': np.array([0, 1]),
    'L': np.array([0, -1]),
    'U': np.array([1, 0]),
    'D': np.array([-1, 0])
}

class ShortRope:
    def __init__(self):
        self.head = np.array([0, 0])
        self.tail = np.array([0, 0])
        self.unique_tail = set()

    def move(self, movement):
        self.head += CARDINALS[movement]
        displacement = self.head - self.tail

        if tuple(displacement) not in ADJACENT:
            self.tail += np.sign(displacement)

        self.unique_tail.add(tuple(self.tail))

if __name__ == '__main__':
    rope = ShortRope()

    with open("input.txt", 'r') as input_file:
        for line in input_file:
            direction, amount = line.strip().split()
            for _ in range(int(amount)):
                rope.move(direction)

    print(f"The tail of the rope moves to {len(rope.unique_tail)} unique positions.")
