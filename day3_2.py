with open('input3', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

claim_map = {}

non_conflicting = set()

for line in puzzle_input:
    non_conflicting.add(int(line[1:].split(' ')[0]))


def claim(owner, start_x, start_y, width, height):
    for i in range(start_x, width+start_x):
        for j in range(start_y, height+start_y):
            if claim_map.get((i, j), 0) != 0:
                non_conflicting.difference_update({owner, claim_map.get((i, j), 0)})
                claim_map[i, j] = owner
            else:
                claim_map[i, j] = owner


for line in puzzle_input:
    claim(int(line[1:].split(' ')[0]),
          int(line[1:].split(':')[0].split(' ')[2].split(',')[0]),
          int(line[1:].split(':')[0].split(' ')[2].split(',')[1]),
          int(line[1:].split(':')[1].strip().split('x')[0]),
          int(line[1:].split(':')[1].strip().split('x')[1]))

double_claims = 0
ones = 0

for value in claim_map.values():
    if value == 2:
        double_claims += 1
    elif value == 1:
        ones += 1


print("answer: " + str(non_conflicting))
