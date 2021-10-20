sequence = list(map(int, input().split()))
result = set()
for el in sequence:
    if el not in result:
        print("NO")
        result.add(el)
    else:
        print("YES")