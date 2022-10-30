n = int(input())

arr = dict()

for _ in range(n):
    t, l, r = map(str, input().split())
    arr[t]= [l,r]

def pre_t(root):
    if root != '.':
        print(root,end='')
        pre_t(arr[root][0])
        pre_t(arr[root][1])
        
def inor_t(root):
    if root != '.':
        inor_t(arr[root][0])
        print(root,end='')
        inor_t(arr[root][1])

def post_t(root):
    if root != '.':
        post_t(arr[root][0])
        post_t(arr[root][1])
        print(root,end='')

pre_t('A')
print()
inor_t('A')
print()
post_t('A')