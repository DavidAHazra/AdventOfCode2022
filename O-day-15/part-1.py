import collections


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_in_range(sensor_dict, x, y):
    for sensor_loc in sensor_dict:
        if grid[(x, y)] != 'B' and manhattan_distance(sensor_loc, (x, y)) <= sensors[sensor_loc]:
            return True

    return False


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [
            line.strip()
            .replace("Sensor at ", '').replace(": closest beacon is at ", ',')
            .replace("x=", "").replace("y=", '').split(',')
            for line in input_file
        ]

    data = [
        (
            (int(line[0]), int(line[1])),
            (int(line[2]), int(line[3]))
        ) for line in lines
    ]

    grid = collections.defaultdict(str)
    min_x, max_x, sensors = 0, 0, dict()
    for sensor_pos, beacon_pos in data:
        grid[beacon_pos] = 'B'

        dist = manhattan_distance(sensor_pos, beacon_pos)
        sensors[sensor_pos] = dist

        min_x = min(min_x, sensor_pos[0] - dist)
        max_x = max(max_x, sensor_pos[0] + dist)

    num_in_range = sum(int(is_in_range(sensors, x, 2000000)) for x in range(min_x, max_x + 1))
    print(f"There are {num_in_range} positions on row 2000000 that cannot contain a beacon.")

