
n = int(input())
number = 0
sortnum = 666
goal = ""

while number != n:
    goal = str(sortnum)
    for i in range(0,len(goal)-2):
        if(goal[i]=='6' and goal[i+1]=='6' and goal[i+2]=='6'):
            number+=1
            break

    if number!=n:
        sortnum+=1

print(sortnum)
            