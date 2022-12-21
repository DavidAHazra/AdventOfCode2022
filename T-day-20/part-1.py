if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        arrangement = [int(line.strip()) for line in input_file]

    permutation = [index for index in range(len(arrangement))]

    # Mixing procedure
    for original_index in range(len(arrangement)):
        mixed_index = permutation.index(original_index)

        value = arrangement.pop(mixed_index)
        insert_pos = (mixed_index + value) % len(arrangement)

        arrangement.insert(insert_pos, value)
        permutation.insert(insert_pos, permutation.pop(mixed_index))

    # Find the grove coordinates
    zero_pos = arrangement.index(0)

    grove_coordinates = [
        arrangement[(zero_pos + 1000) % len(arrangement)],
        arrangement[(zero_pos + 2000) % len(arrangement)],
        arrangement[(zero_pos + 3000) % len(arrangement)]
    ]

    print(f"The sum of the grove coordinates is: {sum(grove_coordinates)}.")
