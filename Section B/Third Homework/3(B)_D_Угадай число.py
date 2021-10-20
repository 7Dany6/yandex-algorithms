n = int(input())
outcomes = set(range(1, n+1))
request = input()
while request != "HELP":
    if request == "YES":
        outcomes.intersection_update(sequence)
    elif request == "NO":
        outcomes.difference_update(sequence)
    else:
        sequence = set(map(int, request.split()))
    request = input()
print(*sorted(outcomes))