from collections import defaultdict
with open('input.txt', 'r') as file_input:
    count = defaultdict(int)
    names = []
    for line in file_input:
        words = line.strip().split()
        for word in words:
            count[word] += 1
    results = [(-value, key) for key, value in count.items()]
    results.sort()
with open('output.txt', 'w') as file_output:
    for el in results:
        file_output.write(el[1]+'\n')