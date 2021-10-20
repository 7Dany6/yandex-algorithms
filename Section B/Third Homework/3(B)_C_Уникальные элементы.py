sequence = list(map(int, input().split()))
for el in sequence:
    if sequence.count(el) > 1:
        continue
    else:
        print(el, end=' ')