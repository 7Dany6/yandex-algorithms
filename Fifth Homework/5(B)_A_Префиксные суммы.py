n, m = map(int, input().split())
array = list(map(int, input().split()))
preffix_sum = [0] * (len(array) + 1)
for i in range(1, len(preffix_sum)):
	preffix_sum[i] = array[i-1] + preffix_sum[i-1]
def return_sum(l, r):
	result = preffix_sum[r] - preffix_sum[l-1]
	return result
for _ in range(m):
	left_bound, right_bound = map(int, input().split())
	print(return_sum(left_bound, right_bound))

