from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    color, number = map(int, input().split())
    dic[color] += number
for key, value in sorted(dic.items(), key=lambda x:x[0]): # made for more sophisticated solution
    print(key, value)
