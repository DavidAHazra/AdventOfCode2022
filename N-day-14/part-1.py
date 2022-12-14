import collections


def simulate_sand(min_col, max_col, max_row):
    # Place a sand grain at (500, 0)
    location = (500, 0)

    # Check sand is not in the abyss
    while (min_col <= location[0] <= max_col) and (0 <= location[1] <= max_row):
        new_row = location[1] + 1

        # Falls straight down
        if grid[(location[0], new_row)] == "":
            location = (location[0], new_row)
            continue

        # Falls down and to the left
        if grid[(location[0] - 1, new_row)] == "":
            location = (location[0] - 1, new_row)
            continue

        # Falls down and to the right
        if grid[(location[0] + 1, new_row)] == "":
            location = (location[0] + 1, new_row)
            continue

        # Sand is at rest
        grid[location] = "+"
        return True

    return False


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        paths = [
            [tuple(map(lambda component: int(component), coord.split(','))) for coord in line.strip().split(" -> ")]
            for line in input_file
        ]

    grid = collections.defaultdict(str)

    # Place rocks
    for path in paths:
        for index in range(len(path) - 1):
            for x in range(min(path[index][0], path[index + 1][0]), max(path[index][0], path[index + 1][0]) + 1):
                for y in range(min(path[index][1], path[index + 1][1]), max(path[index][1], path[index + 1][1]) + 1):
                    grid[(x, y)] = '#'

    # Get bounds of area
    bottom_row, left_boundary, right_boundary = 0, float('inf'), float('-inf')
    for col, row in grid:
        bottom_row = max(bottom_row, row)
        left_boundary, right_boundary = min(left_boundary, col), max(right_boundary, col)

    # Simulate
    sand_placed = 0
    while True:
        placed = simulate_sand(left_boundary, right_boundary, bottom_row)
        if not placed:
            break

        sand_placed += 1

    print(f"{sand_placed} sand fell before the next fell into the abyss.")
