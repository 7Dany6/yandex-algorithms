n, m = map(int, input().split())
pupils_in_groups = sorted([(value, index) for index, value in enumerate(list(map(int, input().split())))])
computers_in_groups = sorted([(value, index+1) for index, value in enumerate(list(map(int, input().split())))])
rooms = [0] * len(pupils_in_groups)
i = j = 0
for students, number in pupils_in_groups:
    while j < len(computers_in_groups) and computers_in_groups[j][0] < students + 1:
        j += 1
    if j == len(computers_in_groups):
        break
    rooms[number] = computers_in_groups[j][1]
    j += 1
print(n - rooms.count(0))
print(*rooms)
