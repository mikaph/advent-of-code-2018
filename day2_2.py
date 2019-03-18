with open('input2', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()


def differences(string1, string2):
    result = []
    for char in range(0, len(string1)):
        if string1[char] != string2[char]:
            result.append(char)

    return result


for i in puzzle_input:
    for j in puzzle_input:
        different_indexes = differences(i, j)
        if len(different_indexes) == 1:
            print("answer: " + i[:different_indexes[0]] + i[different_indexes[0]+1:])
