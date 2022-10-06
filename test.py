

nums = [1,2,3,4,5,6,7]
answer = 0
n=3000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
for i in nums:
    if i in primes:
        answer+=1
print(answer)