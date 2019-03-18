with open('input3', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

claim_map = {}


def claim(start_x, start_y, width, height):
    for i in range(start_x, width+start_x):
        for j in range(start_y, height+start_y):
            if claim_map.get((i, j), 0) == 1 or claim_map.get((i, j), 0) == 2:
                claim_map[i, j] = 2
            else:
                claim_map[i, j] = 1


for line in puzzle_input:
    claim(int(line[1:].split(':')[0].split(' ')[2].split(',')[0]),
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


print("answer: " + str(double_claims))
