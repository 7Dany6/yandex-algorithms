L, K = map(int, input().split())
middle = len(L) / 2
to_delete = 0
for _ in range(K):
    arguments = list(map(int, input().split()))
if K == 1:
    print(arguments[0])
else:
    for i in range(K):
        if i < middle:
            to_delete = i
        elif i == middle:
            if len % 2 != 0:
                print(arguments[to_delete])
            else:
                print(f'{arguments[to_delete]} {arguments[i]}')
        else:
            print(f'{arguments[to_delete]} {arguments[i]}')