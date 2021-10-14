string = input()
n_changes = 0
if len(string) == 1:
    print(n_changes)
else:
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            n_changes += 1
    print(n_changes)