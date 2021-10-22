def count_elements(array:list):
    count = 0
    for el in range(1, len(array)-1):
        if array[el] > array[el-1] and array[el] > array[el+1]:
            count += 1
    return count

sequence = list(map(int, input().split()))
print(count_elements(sequence))
