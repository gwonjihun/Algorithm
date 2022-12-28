n = int(input())
budget = list(map(int,input().split()))
total_Get = int(input())

start, end = 0, max(budget)
total_budget = 0

if total_Get >= sum(budget):
    print(max(budget))
else:
    while start <=end:
        mid = (start+end)//2

        total_budget = 0
        for i in budget:
            total_budget+= min(mid,i)
        
        if total_budget > total_Get:
            end = mid- 1
        else:
            start = mid+1
    print(end)