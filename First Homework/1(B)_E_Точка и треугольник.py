d = int(input())
x, y = map(int, input().split())
if x >= 0 and y >= 0 and x + y <= d:
	print(0)
else:
    distances = [(x**2 + y**2, 1), ((x-d)**2 + y**2, 2), (x**2 + (y-d)**2, 3)]
    print(min(distances, key=lambda x: x[0])[1])
