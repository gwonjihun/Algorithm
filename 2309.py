a = []
for _ in range(0,9):
    a.append(int(input()))
sum=0
for i in range(0,9):
    sum += a[i]
# 
a.sort()
one = 0 
two = 0

for i in range(0,9):
    for j in range(i+1,9): 
        if((sum-a[i]-a[j])==100):
            one = a[i]
            two = a[j]

a.remove(one)
a.remove(two)
for sd in a:
    print(sd)
                
         
         