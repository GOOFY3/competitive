n = int(raw_input())
arr = raw_input().split(' ')

for i in range(0, int(n)):
    arr[i] = int(arr[i])

count = 0
arr.sort()

for i in xrange(0, n/2 + 1, 2):
    if arr[i] != arr[i+1]:
        print(arr[i])
        count +=1
    else:
        continue

if count == 0:
    print(arr[n-1])
