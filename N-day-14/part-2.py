import collections


def simulate_sand(floor):
    # Place a sand grain at (500, 0)
    location = (500, 0)

    while True:
        new_row = location[1] + 1
        if new_row == floor:
            break

        # Falls straight down
        if grid[(location[0], new_row)] == "":
            location = (location[0], new_row)
            continue

        # Falls down and to the left
        if grid[(location[0] - 1, new_row)] == "":
            location = (location[0] - 1, new_row)
            continue

        # Falls down and to the right
        if grid[(location[0] + 1, location[1] + 1)] == "":
            location = (location[0] + 1, new_row)
            continue

        # Sand is at rest since it can't move
        break

    grid[location] = "+"
    return location


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

    # Find where the floor is
    max_row = 0
    for _, row in grid:
        max_row = max(max_row, row)

    floor_row = max_row + 2

    # Simulate
    sand_placed = 0
    while True:
        sand_placed += 1
        placed_location = simulate_sand(floor_row)
        if placed_location == (500, 0):
            break

    print(f"{sand_placed} sand was placed until the source location was blocked.")
