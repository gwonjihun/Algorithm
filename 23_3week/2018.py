n = int(input())
s,e = 1,1
cnt,total = 0,1

while e < n:
    if total <n :
        e += 1
        total += e
    elif total > n :
        total -= s
        s += 1
    else:
        cnt +=1
        e +=1
        total+= e

print(cnt +1)