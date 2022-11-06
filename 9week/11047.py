n, k = map(int,input().split())

arr = [0]* n
count = 0
for i in range(n-1,-1,-1):
    arr[i] = int(input())

for i in range(0,n):
    if k//arr[i]!=0:
        count += k//arr[i]
        k = k%arr[i]
print(count)