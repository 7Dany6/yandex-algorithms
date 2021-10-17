from collections import defaultdict


def find(s, a, b, c):
    length_a, *a = a
    length_b, *b = b
    length_c, *c = c
    dic_c = defaultdict(list)
    for el in range(len(c)):
        dic_c[c[el]].append(el)
    for i in range(len(a)):
        for j in range(len(b)):
            if (s - a[i] - b[j]) in dic_c:
                print(i, j, min(dic_c[s - a[i] - b[j]]))
                return
    print(-1)


s = int(input())
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
find(s, a, b, c)
