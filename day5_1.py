with open('input5', 'r') as input_file:
    puzzle_input = input_file.read()


def react(polymer):
    for i in range(0, len(polymer)-1):
        if len(polymer) < 2:
            return polymer
        if (polymer[i].isupper() ^ polymer[i+1].isupper()) and polymer[i].lower() == polymer[i+1].lower():
            return polymer[:i] + polymer[i+2:]

    return polymer


while len(react(puzzle_input)) < len(puzzle_input):
    print(len(puzzle_input))
    puzzle_input = react(puzzle_input)

print("answer:" + str(len(puzzle_input.strip())))
