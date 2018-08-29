inp = raw_input().split(' ')
n = int(inp[0])
k = int(inp[1])

arr = raw_input().split(' ')

for i in range(0, len(arr)):
    arr[i] = int(arr[i])

count = 0
res = list()
for i in range(1, k+1):
    pos = 0
    for j in range(0, n):
        if arr[j] == 0:
            pos = pos + i
            if pos == n:
                count += 1
                break
            else:
                continue
        elif arr[j] == 1:
            pos += 1

print(count)            
