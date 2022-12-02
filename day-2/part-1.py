# (Rock, Paper), (Paper, Scissors), (Scissors, Rock)
WINNING_PAIRS = {('A', 'B'), ('B', 'C'), ('C', 'A')}


def simulate_permutation(input_tuples, strategy):
    simulated_score = 0
    for their_move, our_move in input_tuples:
        our_move = strategy[our_move]

        simulated_score += ord(our_move) - 64
        if their_move == our_move:
            simulated_score += 3

        elif (their_move, our_move) in WINNING_PAIRS:
            simulated_score += 6

    return simulated_score


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        games = [line.strip().split(' ') for line in input_file]

    strategy_guide = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    score = simulate_permutation(games, strategy_guide)

    print(f"Using the suggested strategy guide, you get a score of {score}.")
