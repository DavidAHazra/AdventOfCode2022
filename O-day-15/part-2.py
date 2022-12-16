import collections
import tqdm


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_in_range(sensor_dict, x, y):
    for sensor_loc in sensor_dict:
        if grid[(x, y)] != 'B' and manhattan_distance(sensor_loc, (x, y)) <= sensors[sensor_loc]:
            return True

    return False


def get_sensor_range(sensor_loc, current_row):
    width = abs(current_row - sensor_loc[1])
    radius = sensors[sensor_loc]

    if width <= radius:
        return [sensor_loc[0] - (radius - width), sensor_loc[0] + (radius - width)]


def get_all_sensor_intervals(wanted_row):
    return list(filter(lambda x: x is not None, [get_sensor_range(sensor, wanted_row) for sensor in sensors]))



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

    sensors = dict()
    for sensor_pos, beacon_pos in data:
        sensors[sensor_pos] = manhattan_distance(sensor_pos, beacon_pos)

    MAX_VAL = 4000000
    for row in tqdm.tqdm(range(0, MAX_VAL + 1)):
        sensor_intervals = get_all_sensor_intervals(row)

        for left_x, right_x in sensor_intervals:
            if 0 <= left_x - 1 <= MAX_VAL:
                if not is_in_range(sensors, left_x - 1, row):
                    print(f"Found a gap in the sensor coverage at {(left_x - 1, row)}.")

            if 0 <= right_x + 1 <= MAX_VAL:
                if not is_in_range(sensors, right_x + 1, row):
                    print(f"Found a gap in the sensor coverage at {(right_x + 1, row)}.")


