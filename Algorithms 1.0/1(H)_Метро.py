def interval(min1, max1, min2, max2):
    minimum = max(min1, min2)
    min_maximum = min(max1, max2)
    if min_maximum < minimum:
        return -1
    return f'{minimum} {min_maximum}'

a, b, n, m = int(input()), int(input()), int(input()), int(input())
minimum1 = n + (n-1) * a
maximum1 = 2 * a + a * (n-1) + n
minimum2 = m + (m-1) * b
maximum2 = 2 * b + b * (m-1) + m
print(interval(minimum1, maximum1, minimum2, maximum2))
