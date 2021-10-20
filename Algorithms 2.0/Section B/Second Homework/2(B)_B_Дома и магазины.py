houses = list(map(int, input().split()))
indexes = [el for el in range(len(houses)) if houses[el] == 2]
indexes_ = [el for el in range(len(houses)) if houses[el] == 1]
result = []
nearest = []
for house in indexes_:
    for shop in indexes:
        result.append(abs(house - shop))
    nearest.append(min(result))
    result.clear()
print(max(nearest))