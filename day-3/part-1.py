def parse_rucksack(rucksack):
    mid_point = len(rucksack) // 2

    return sum(
        ord(parcel) - 96 if parcel.islower() else ord(parcel) - 38
        for parcel in set(rucksack[:mid_point]) & set(rucksack[mid_point:])
    )

if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        rucksack_sum = sum(parse_rucksack(line.strip()) for line in input_file)

    print(f"The sum of the mixed up item type priorities is {rucksack_sum}.")

