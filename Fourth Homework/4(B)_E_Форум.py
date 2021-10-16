from collections import Counter
n = int(input())
topics = []
answers = [0] * n
for i in range(n):
    number = int(input())
    if number == 0:
        topic = input()
        input()
        topics.append(topic)
        answers[i] = i
    else:
        answers[i] = answers[number-1]
        input()
count = []
result = Counter(answers)
for key, value in result.items():
    count.append((-value, key))
count.sort()
print(topics[count[0][1]])
