tc= int(input())
for _ in range(tc):
    s_x, s_y, e_x,e_y = map(int,input().split())

    c_t = int(input())

    arr = [ list(map(int,input().split())) for _ in range(c_t)]
    cnt = 0
    for x,y,d in arr:
        d1 = (((s_x - x) ** 2) + ((s_y-y)**2))**0.5
        d2 = (((e_x - x) ** 2) + ((e_y-y)**2))**0.5
        if (d1 < d and d2 > d) or (d1 > d and d2 <d):
            cnt+=1

    print(cnt)

    