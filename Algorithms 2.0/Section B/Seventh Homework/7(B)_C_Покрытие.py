m = int(input())
left, right = map(int, input().split())
suitable = []
while left != 0 or right != 0:
    if right > 0 and left < m:
        suitable.append((left, right))
    left, right = map(int, input().split())
suitable.sort()
answers = []
current_right_boarder = 0
possible_right_boarder = 0
the_best = (0, 0)
for el in suitable:
    if el[0] > current_right_boarder:
        answers.append(the_best)
        current_right_boarder = possible_right_boarder
        if current_right_boarder >= m:
            break
    if el[0] <= current_right_boarder and el[1] > possible_right_boarder:
        possible_right_boarder = el[1]
        the_best = el
if current_right_boarder < m:
    current_right_boarder = possible_right_boarder
    answers.append(the_best)
if current_right_boarder < m:
    print("No solution")
else:
    print(len(answers))
    for answer in answers:
        print(*answer)
