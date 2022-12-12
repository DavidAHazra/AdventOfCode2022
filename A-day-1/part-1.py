if __name__ == '__main__':
    max_calories, current_calories = 0, 0
    with open("input.txt", 'r') as input_file:
        for line in input_file:
            if line == '\n':
                max_calories = max(max_calories, current_calories)
                current_calories = 0
                continue

            current_calories += int(line)

    print(f"The elf carrying the most calories has {max_calories} calories.")
