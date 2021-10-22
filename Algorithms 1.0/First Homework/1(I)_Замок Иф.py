def compare(side1, side2, side3, side4):
    return "YES" if (side1 >= side3) and (side2 >= side4) else "NO"


a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
shortest, longest = sorted([d, e])
short_brick, long_brick, *other = sorted([a, b, c])
print(compare(shortest, longest, short_brick, long_brick))
