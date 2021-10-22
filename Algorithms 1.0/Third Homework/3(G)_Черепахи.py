def turtles(n:int, answers:list):
    count = 0
    given_answers = set()
    for el in answers:
        if el[0] < 0 or el[1] < 0 or el[0] + el[1] + 1 != n:
            continue
        if el[0] + el[1] + 1 == n and (el[0], el[1]) not in given_answers:
            count += 1
            given_answers.add((el[0], el[1]))
    return count


number = int(input())
coordinates = []
for _ in range(number):
    coordinates.append(list(map(int, input().split())))
print(turtles(number, coordinates))
