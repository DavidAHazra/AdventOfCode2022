def decrypt_simulate(input_tuples):
    simulated_score = 0

    for their_move, outcome in input_tuples:
        our_move = {
            'X': {'A': 'C', 'B': 'A', 'C': 'B'}[their_move],
            'Y': their_move,
            'Z': {'A': 'B', 'B': 'C', 'C': 'A'}[their_move]
        }[outcome]

        simulated_score += 3 * ord(outcome) + ord(our_move) - 328

    return simulated_score


if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        games = [line.strip().split(' ') for line in input_file]

    score = decrypt_simulate(games)
    print(f"After decrypting the strategy guide, you get a score of {score}.")
