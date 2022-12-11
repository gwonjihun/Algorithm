n = int(input())

arr =[list(map(int,input().split())) for _ in range(n)]


# print(arr)

glo_zero = 0
glo_min = 0
glo_one = 0

def check_box(x,y,n):
    global glo_zero,glo_one,glo_min
    check = arr[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        check_box(x+k*n//3,y+l*n//3,n//3)
                return

    if check == -1:
        glo_min +=1
    elif check == 0:
        glo_zero+=1
    else:
        glo_one+=1

check_box(0,0,n)
print(glo_min)
print(glo_zero)
print(glo_one)