N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)


for i in range(M):
    if A[i] < B[i]:
        A[i] , B[i] = B[i] , A[i]
    else:
        break
print(A)
print(sum(A))
