num = input()
a = input().split()

max = int(a[0])
min = int(a[0])

cmax = 0
cmin = 0

for i in range(1, int(num)):
    if int(a[i]) > max:
        cmax += 1
        max = int(a[i])
    elif int(a[i]) < min:
        cmin += 1
        min = int(a[i])
    else:
        continue

print(cmax, cmin)
