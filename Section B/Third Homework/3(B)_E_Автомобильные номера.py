N = int(input())
witnesses = []
for _ in range(N):
    witnesses.append(set(input()))
numbers = []
count = 0
M = int(input())
maxcount = 0
for _ in range(M):
    number = input()
    number_set = set(number)
    for el in witnesses:
        if el.issubset(number_set):
            count += 1
    numbers.append((number, count))
    if count > maxcount:
        maxcount = count
    count = 0
for element in numbers:
    if element[1] == maxcount:
        print(element[0])
