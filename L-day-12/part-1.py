import collections


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        grid = [line.strip() for line in input_file]

    # Find starting point
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)
                break

    assert start is not None

    # Perform BFS to find end point
    queue = collections.deque([(start, 0)])
    visited = {start}

    while queue:
        (i, j), num_steps = queue.popleft()

        if grid[i][j] == 'E':
            print(f"The fastest path from the starting point to the end takes {num_steps} steps.")
            break

        for adj_i, adj_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            pos = (adj_i, adj_j)
            if 0 <= adj_i < len(grid) and 0 <= adj_j < len(grid[0]) and pos not in visited:
                if grid[i][j] == 'S' or ord(grid[adj_i][adj_j]) <= ord(grid[i][j]) + 1:
                    queue.append((pos, num_steps + 1))
                    visited.add(pos)
