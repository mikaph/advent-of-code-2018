with open('input2', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()


def freqs(string):
    result = {}
    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result.update({letter: 1})

    return result


pairs = 0
triples = 0

for i in puzzle_input:
    pair_found = False
    triple_found = False
    frequencies = freqs(i)
    for key in frequencies:
        if frequencies.get(key) == 2 and not pair_found:
            pairs += 1
            pair_found = True
        if frequencies.get(key) == 3 and not triple_found:
            triples += 1
            triple_found = True


print("answer: " + str(pairs*triples))
