N, i, j = map(int, input().split())
distance_1 = abs(j - i) - 1
distance_2 = N - distance_1 - 2
print(min(distance_1, distance_2))
