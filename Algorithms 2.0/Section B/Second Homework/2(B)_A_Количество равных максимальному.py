result = []
while True:
    number = int(input())
    if number == 0:
        break
    result.append(number)
el_max = max(result)
print(result.count(el_max))