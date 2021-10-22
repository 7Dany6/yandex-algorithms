def find_coords(number:int, coords:list):
    x_es = set()
    for el  in coords:
        x_es.add(el[0])
    return len(x_es)


n = int(input())
coordinates = []
for _ in range(n):
    coordinates.append(list(map(int, input().split())))
print(find_coords(n, coordinates))
