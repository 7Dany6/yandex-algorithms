from functools import reduce

n = int(input())
diploms = list(map(int, input().split()))
print(reduce(lambda x,y: x + y, diploms) - max(diploms))