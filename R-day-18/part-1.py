import collections
import functools


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
        coordinates = [tuple(map(lambda x: int(x), line.strip().split(','))) for line in input_file]

    adj_list = collections.defaultdict(set)
    for i in range(len(coordinates)):
        adj_list[coordinates[i]] = set()

        for j in range(len(coordinates)):
            if coordinates[i] in get_adjacent(coordinates[j]):
                adj_list[coordinates[i]].add(coordinates[j])
                adj_list[coordinates[j]].add(coordinates[i])

    num_uncovered = 6 * len(coordinates) - sum(len(adj_list[point]) for point in adj_list)
    print(f"The surface area of the lava droplet is: {num_uncovered}.")
