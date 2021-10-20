def count(length, number_of_legs, array_legs):
    to_save = 0
    middle = length // 2
    if len(array_legs) == 1:
        return array_legs[0]
    for leg in range(number_of_legs):
        if array_legs[leg] < middle:
            to_save = leg
        elif array_legs[leg] == middle and length % 2 != 0:
                return array_legs[leg]
        else:
            return '{} {}'.format(array_legs[to_save], array_legs[leg])

L, K = map(int, input().split())
legs = list(map(int, input().split()))
print(count(L, K, legs))


