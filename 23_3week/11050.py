def factorial(i : int):
    sum = 1
    for j in range(1,i+1):
        sum *= j

    return sum

N, k = map(int,input().split())

print(factorial(N)//factorial(N-k)//factorial(k))