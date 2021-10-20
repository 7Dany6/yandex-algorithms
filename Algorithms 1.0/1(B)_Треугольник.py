def triangle_equality(first, second, third):
    return "YES" if (first + second > third) and (second + third > first) and (first + third > second) else "NO"

a, b, c = int(input()), int(input()), int(input())
print(triangle_equality(a, b, c))
