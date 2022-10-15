n = int(input())
m = list(map(int,input().split()))
leader, worker = map(int,input().split())
people = 0

for i in m:
    i = i - leader*1
    people += i//worker+1
    if i%worker !=0:
        people+=1

print(people)
