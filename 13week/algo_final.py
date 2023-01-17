# 
# 8
#  5 7 1 3 6 4 8 9


n = int(input())

array = list(map(int, input().split()))

d = [1]*n

result_arr = [[] for _ in range(n)]

result = 0

for i in range(1, n):
    for j in range(i):

        if array[j] < array[i]:
            if d[i] >= (d[j]+1) :
                result_arr[i] = result_arr[j][:]
            else:
                result_arr[i].append(array[j])
            d[i] = max(d[i], d[j]+1)
    result_arr[i].append(array[i])

max_d = max(d)

for i in result_arr[d.index(max_d)]:
    print(i, end=' ')

print()
print(max_d)