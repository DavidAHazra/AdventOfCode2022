def get_priority(parcel):
    return ord(parcel) - 96 if parcel.islower() else ord(parcel) - 38


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        lines = [line.strip() for line in input_file]

    badge_sum = sum(
        get_priority((set(lines[index]) & set(lines[index + 1]) & set(lines[index + 2])).pop())
        for index in range(0, len(lines), 3)
    )

    print(f"The sum of the Elf groups' badge item types is {badge_sum}.")
