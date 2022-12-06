if __name__ == '__main__':
    with open("input.txt", 'r') as input_file:
        sequence = input_file.read()

    packet_marker = None
    for i in range(len(sequence) - 4):
        if len(set(sequence[i:i+4])) == 4:
            packet_marker = i + 4
            break

    print(f"{packet_marker} characters need to be processed before the first start-of-packet marker is detected.")
