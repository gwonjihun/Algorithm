def combinate(arr,j,result):
    if len(result) == 6:
        for i in result:
            print(i, end=' ')
        print()
        return
    else:
        temp = result[:]
        if j < len(arr):
            temp.append(arr[j])
            combinate(arr,j+1,temp)
            # print(temp)
            combinate(arr,j+1,result)


        else:
            return
inputs = list(map(int,input().split()))

while inputs[0] != 0:
    n = inputs[0]
    arr = inputs[1:]
    arr = sorted(arr)
    # print(arr)
    result=[]
    combinate(arr,0,result)
    print()
    inputs = list(map(int,input().split()))