n = raw_input()
arr = [0]*int(n)
for i in range(0, int(n)):
    arr[i] = raw_input().split(' ')

c = [0]*int(n)
r = [0]*int(n)
for i in range(0,int(n)):
    c[i] = (arr[i])[0]
    r[i] = (arr[i])[1]

count = 0

for i in range(0,int(n)):
    for j in range(i+1,int(n)):
        if int(c[i]) + int(r[i]) == int(c[j]) - int(r[j]):
            count = count + 1
        else:
            continue
print(count)
