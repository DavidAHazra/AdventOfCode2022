if __name__ == '__main__':
    contains = 0
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            elf_a, elf_b = line.strip().split(",")
            a_lower, a_upper = map(lambda x: int(x), elf_a.split("-"))
            b_lower, b_upper = map(lambda x: int(x), elf_b.split("-"))
            contains += not (a_lower > b_upper or b_lower > a_upper)

    print(f"There are {contains} pairs of elves with overlapping assignments.")
