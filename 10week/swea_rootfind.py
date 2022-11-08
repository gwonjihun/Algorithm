n = int(input())
s = 0
while s!=n:
    s+=1
    row= [0]*8
    col = [0]*8
    arr =[]
    for _ in range(8):
        arr.append(input())
    count = 0
    for i in range(0,8):
        for j in range(0,8):    
            if arr[i][j] == 'O':
                row[i]=1
                col[j]=1
                count+=1
    if count == 8 and 0 not in row and 0 not in col:
        print(f'#{s} yes')
    else:
        print(f'#{s} no')

