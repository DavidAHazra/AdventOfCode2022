import heapq


min_heap, current_calories = [], 0
with open("input.txt", 'r') as input_file:
    for line in input_file:
        if line == '\n':
            heapq.heappush(min_heap, current_calories)

            while len(min_heap) > 3:
                heapq.heappop(min_heap)

            current_calories = 0
            continue

        current_calories += int(line)


print("The top 3 elves carrying the most calories have:")

total_calories = 0
for index in range(3):
    current_elf = heapq.heappop(min_heap)
    total_calories += current_elf
    print(f"\t{3 - index}) {current_elf}")


print(f"\nCombined, they carry {total_calories} calories.")