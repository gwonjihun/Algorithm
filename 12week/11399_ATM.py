n = int(input())
arr = list(map(int,input().split()))

arr.sort()
sumsss =0
result = []
# print(arr)
# print(sum([1]))
for i in range(0,n):
    if len(arr[:i+1]) == 1 :
        result.append(arr[0])
        continue
    result.append(sum(arr[:i+1]))
# print(result)
sumsss = sum(result)
print(sumsss)