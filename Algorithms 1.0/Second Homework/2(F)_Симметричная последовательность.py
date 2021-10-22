def symmetry(array: list):
    if array == array[::-1]:
        print(0)
        return
    for start in range(len(array)):
        i = start
        j = len(array) - 1
        while i < len(array) and j >= 0 and array[i] == array[j] and j >= i:
            i += 1
            j -= 1
        if i > j:
            result = []
            for i in range(start-1, -1, -1):
                result.append(array[i])
            print(len(result), '\n', *result)
            return


n = int(input())
arr = list(map(int, input().split()))
symmetry(arr)
