with open('input1', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

freq = 0

for number in puzzle_input:
    freq += int(number)

print("answer:" + str(freq))
