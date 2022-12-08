if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        grid = [list(map(lambda x: int(x), line.strip())) for line in input_file]

    # Maintain an array detailing the tallest tree in each direction from each position
    tallest_state = [[[0, 0, 0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if col == 0:
                tallest_state[row][col][0] = -1
                continue

            tallest_state[row][col][0] = max(grid[row][col - 1], tallest_state[row][col - 1][0])

        for col in range(len(grid[0]) - 1, -1, -1):
            if col == len(grid[0]) - 1:
                tallest_state[row][col][1] = -1
                continue

            tallest_state[row][col][1] = max(grid[row][col + 1], tallest_state[row][col + 1][1])

    for col in range(len(grid[0])):
        for row in range(len(grid)):
            if row == 0:
                tallest_state[row][col][2] = -1
                continue

            tallest_state[row][col][2] = max(grid[row - 1][col], tallest_state[row - 1][col][2])

        for row in range(len(grid) - 1, -1, -1):
            if row == len(grid) - 1:
                tallest_state[row][col][3] = -1
                continue

            tallest_state[row][col][3] = max(grid[row + 1][col], tallest_state[row + 1][col][3])

    num_visible = sum(
        any(grid[i][j] > tallest_state[i][j][d] for d in range(4))
        for j in range(len(grid[0]))
        for i in range(len(grid))
    )

    print(f"There are {num_visible} visible trees in this forest.")