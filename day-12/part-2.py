import collections


def search_starting(start):
    # BFS O(mn) | O(mn)

    visited = set()
    queue = collections.deque([(start, 0)])
    visited.add(start)

    while queue:
        (i, j), num_steps = queue.popleft()

        if grid[i][j] == 'E':
            return num_steps

        for adj_i, adj_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            pos = (adj_i, adj_j)
            if 0 <= adj_i < len(grid) and 0 <= adj_j < len(grid[0]) and pos not in visited:
                if grid[i][j] == "S":
                    queue.append((pos, num_steps + 1))
                    visited.add(pos)

                elif ord(grid[adj_i][adj_j]) <= ord(grid[i][j]) + 1:
                    queue.append((pos, num_steps + 1))
                    visited.add(pos)

if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        grid = [line.strip() for line in input_file]

    # Get all starting points O(mn) | O(mn)
    starts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "a":
                starts.append((y, x))

    # Search for end from each starting point
    shortest_length = float('inf')
    for start in starts:
        num_steps = search_starting(start)
        if num_steps:
            shortest_length = min(shortest_length, num_steps)

    print(f"The shortest path between any starting point and the end has length {shortest_length}.")
