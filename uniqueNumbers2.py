n = int(raw_input())
arr = [0]*n
j = 0

arr = raw_input().split(' ')

for i in range(0,n):
    arr[i] = int(arr[i])
arr.sort()
def pair(a):
    global j
    while j < n:
        if a[j] == a[j+1]:
            j = j+2
            pair(a[j])
        elif a[j] != a[j+1]:
            print(a[j])
            j = j+1
            pair(arr[j])
        else:
            print(a[j])
pair(arr)
