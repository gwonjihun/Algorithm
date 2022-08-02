import sys
input=sys.stdin.readline

case = int(input())
while case !=0:
    N = int(input())

    gx=0
    for i in range(1,N+1):
        gx += (N//i)*i

    print(gx)
    case -= 1
