with open('input5', 'r') as input_file:
    puzzle_input = input_file.read()


def react(polymer):
    for i in range(0, len(polymer)-1):
        if len(polymer) < 2:
            return polymer
        if (polymer[i].isupper() ^ polymer[i+1].isupper()) and polymer[i].lower() == polymer[i+1].lower():
            return polymer[:i] + polymer[i+2:]

    return polymer


def react_all(polymer):
    while len(react(polymer)) < len(polymer):
        polymer = react(polymer)
    return polymer


unit_list = set(puzzle_input.lower().strip())

print(str(unit_list))

final_lengths = {}

for unit in unit_list:
    print("letter:" + str(unit))
    final_lengths.update({unit: len(react_all(puzzle_input.replace(unit, "").replace(unit.upper(), "")).strip())})

print(str(final_lengths))
print("answer:" + str(min(final_lengths, key=final_lengths.get)))
