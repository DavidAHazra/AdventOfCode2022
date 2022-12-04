if __name__ == '__main__':
    fully_contain = 0
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            elf_a, elf_b = line.strip().split(",")
            a_lower, a_upper = map(lambda x: int(x), elf_a.split("-"))
            b_lower, b_upper = map(lambda x: int(x), elf_b.split("-"))
            fully_contain += (a_lower <= b_lower and b_upper <= a_upper) or (b_lower <= a_lower and a_upper <= b_upper)

    print(f"There are {fully_contain} pairs of elves where one Elf's assignment fully contains the other.")
