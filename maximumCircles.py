n = int(raw_input())
arr = [0]*int(n)
for i in range(0, int(n)):
    arr[i] = raw_input().split(' ')

c = [0]*n
r = [0]*n
for i in range(0,int(n)):
    c[i] = int((arr[i])[0])
    r[i] = int((arr[i])[1])

count = 1
temp = c[0] + r[0]
for i in range(1, n):
    if c[i] - r[i] >= temp:
        temp = c[i] + r[i]
        count += 1
    else:
        continue
print(n-count)
