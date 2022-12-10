n = int(input())

arr =[list(map(int,input())) for _ in range(n)]

# print(arr)

def check_dif(x,y,n):
    check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != arr[i][j]:
                check = -1
                return -1
    return check

def check_box(x,y,n):
    check = check_dif(x,y,n)

    if check == -1:
        print("(",end="")
        n = n//2
        check_box(x,y,n)
        check_box(x,y+n,n)
        check_box(x+n,y,n)
        check_box(x+n,y+n,n)
        print(")",end="")
    
    elif check == 1:
        print(1,end="")
    else:
        print(0,end="")

check_box(0,0,n)