N = int(input())

shop = list(map(int,input().split()))
shop.sort()
m = int(input())
buy_list = list(map(int,input().split()))
def binary_search(arr,key,start,end):
    while start<= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return False
for i in buy_list:
    start, end = 0, len(shop)-1
    if binary_search(shop,i,start,end):
        print('YES', end=' ')
    else:
        print('NO', end=' ')