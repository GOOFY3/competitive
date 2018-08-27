n = int(raw_input())
arr = [0]*n

arr = raw_input().split(' ')

for i in range(0,n):
    arr[i] = int(arr[i])
res = list()

res = arr[0]
for i in arr:
    res = res^(i+1)

print(res)
