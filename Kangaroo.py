x1,v1,x2,v2 = input().split()

count = 0
r1 = int(x1) + int(v1)
r2 = int(x2) + int(v2)

if x1 > x2 and v1 > v2 or x2 > x1 and v2 > v1:
    print("NO")
else:
    for i in range(1, 10000):
        if r1 == r2:
            print("YES")
            count = count + 1
            break
        else:
            r1 = r1 + int(v1)
            r2 = r2 + int(v2)

if count == 0:
    print("NO")
