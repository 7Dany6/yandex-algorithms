from collections import defaultdict
with open('input.txt', 'r') as file_input:
    candidates = defaultdict(int)
    for line in file_input:
        surname, number = line.split()
        candidates[surname] += int(number)
with open('output.txt', 'w') as output_file:
    for key, value in sorted(candidates.items()):
        output_file.write("%s %s\n" % (key, value))
