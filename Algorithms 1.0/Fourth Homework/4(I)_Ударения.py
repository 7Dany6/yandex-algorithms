from collections import defaultdict
def stresses(stress_dictionary: list, sequence: list):
    counter = 0
    stress_count = 0
    for el in sequence:
        if el.lower() in stress_dictionary:
            if el in stress_dictionary[el.lower()]:
                continue
            counter += 1
        elif el.lower() not in stress_dictionary:
            for char in el:
                if char.isupper():
                    stress_count += 1
            if stress_count != 1:
                counter += 1
            stress_count = 0
    return counter


number = int(input())
stress_dict = defaultdict(list)
for _ in range(number):
    word = input()
    stress_dict[word.lower()].append(word)
sequence = input().split()
print(stresses(stress_dict, sequence))
