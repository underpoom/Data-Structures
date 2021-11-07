def bs(left,right,l,k):
    if left > right:
        return False
    mid = (right + left)//2
    if l[mid] == k:
        return True
    return bs(mid+1,right,l,k) if l[mid] < k else bs(left,mid-1,l,k)
   

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
arr = sorted(arr)
for i in k:
    i=i+1
    while bs(0, len(arr) - 1, arr ,i) is False and i<max(arr):
        i+=1
    if i>max(arr):
        print('No First Greater Value')
    else:
        print(i)