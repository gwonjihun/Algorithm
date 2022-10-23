def sosu(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i ==0:
            return False
    return True
while True:
    m = int(input())
    if m==0:
        break
    count = 0
    for i in range(m,2*m):
        if sosu(i):
            count +=1

    print(count)