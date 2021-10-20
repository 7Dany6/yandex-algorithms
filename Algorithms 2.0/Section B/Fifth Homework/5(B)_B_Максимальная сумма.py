n = int(input())
array = list(map(int, input().split()))
preffix_sum = [0] * (len(array) + 1)
min_value_index = 0
max_value_index = 0
max_sum = 0
for i in range(1, len(preffix_sum)):
    preffix_sum[i] = preffix_sum[i-1] + array[i-1]
    if preffix_sum[i-1] < preffix_sum[min_value_index]:
        min_value_index = i - 1
    current_sum = preffix_sum[i] - preffix_sum[min_value_index]
    if current_sum > max_sum:
        max_sum = current_sum
        max_value_index = i
print(max_sum)
