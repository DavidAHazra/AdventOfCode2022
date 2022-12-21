import functools
import numpy as np




@functools.cache
def get_adjacent(a):
    return {
        (a[0] + 1, a[1], a[2]),
        (a[0] - 1, a[1], a[2]),
        (a[0], a[1] + 1, a[2]),
        (a[0], a[1] - 1, a[2]),
        (a[0], a[1], a[2] + 1),
        (a[0], a[1], a[2] - 1)
    }


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        cube_coordinates = [tuple(map(lambda x: int(x), line.strip().split(','))) for line in input_file]

    grid = set(cube_coordinates)

    # Idea: create a 'container' 1 block away from each edge
    # Then DFS the container with water, keeping track of the number of edges where it touches the lava

    min_coordinate = np.array(cube_coordinates).min(axis=0) - 1
    max_coordinate = np.array(cube_coordinates).max(axis=0) + 1

    num_seen = 0
    stack, visited = [tuple(min_coordinate)], {tuple(min_coordinate)}
    while stack:
        current_point = stack.pop()

        for adj_coord in get_adjacent(current_point):
            if (min_coordinate[0] <= adj_coord[0] <= max_coordinate[0]) and (min_coordinate[1] <= adj_coord[1] <= max_coordinate[1]) and (min_coordinate[2] <= adj_coord[2] <= max_coordinate[2]):
                if adj_coord in grid:
                    num_seen += 1
                    continue

                if adj_coord in visited:
                    continue

                stack.append(adj_coord)
                visited.add(adj_coord)

    print(f"The exterior surface area of the lava droplet is: {num_seen}.")
