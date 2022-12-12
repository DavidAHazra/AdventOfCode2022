if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        sequence = input_file.read()

    message_marker = None
    for i in range(len(sequence) - 14):
        if len(set(sequence[i: i + 14])) == 14:
            message_marker = i + 14
            break

    print(f"{message_marker} characters need to be processed before the first start-of-message marker is detected.")
