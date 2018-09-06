n = int(raw_input())
arr = raw_input().split(' ')

for i in  range(0, n):
    arr[i] = int(arr[i])

sum = 0

for i in range(0,n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            sum = sum + arr[j]
    

print(sum%1000000007)
