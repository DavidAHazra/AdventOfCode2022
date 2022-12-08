import math

def simulate(view, i, j):
    # Time: O(n + m) | Space: O(1)
    our_height = view[i][j]
    visible = [0, 0, 0, 0]

    if j > 0:
        for new_j in range(j - 1, -1, -1):
            visible[0] += 1
            if view[i][new_j] >= our_height:
                break

    if i > 0:
        for new_i in range(i - 1, -1, -1):
            visible[1] += 1
            if view[new_i][j] >= our_height:
                break

    if j < len(view[0]) - 1:
        for new_j in range(j + 1, len(view[0])):
            visible[2] += 1
            if view[i][new_j] >= our_height:
                break

    if i < len(view) - 1:
        for new_i in range(i + 1, len(view)):
            visible[3] += 1
            if view[new_i][j] >= our_height:
                break

    return math.prod(visible)

if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        grid = [list(map(lambda x: int(x), line.strip())) for line in input_file]

    # Time: O(mn) * O(m + n) = O(m^2n + n^2m) = O(m^2) + O(n ^2 )
    best_scenery = max(max(simulate(grid, a, b) for b in range(len(grid[0]))) for a in range(len(grid)))
    print(f"The tree with the highest scenery score has a score of {best_scenery}.")
