with open('input1', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

freq = 0
freqs = []
no_duplicates = True

while no_duplicates:
    for number in puzzle_input:
        freqs.append(freq)
        freq += int(number)
        if freq in freqs:
            print("answer2:" + str(freq))
            no_duplicates = False
            break
