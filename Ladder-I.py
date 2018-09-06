inp = raw_input().split(' ')
n = int(inp[0])
k = int(inp[1])

arr = raw_input().split(' ')

for i in range(0, len(arr)):
    arr[i] = int(arr[i])


count = 0


for i in range(1, k+1):
    pos = 0
    while pos <= n-1:
        if arr[pos] == 0:
            if pos == n-1:
                count += 1
                break
            else:
                pos = pos + i


        elif arr[pos] == 1:
            pos = pos - i
            if i + 1 <= k:
                pos = pos + i + 1
            if pos == n - 1:
                count += 1
                break

print(count)
