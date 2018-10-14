n = int(input())
inp = input().split(" ")
a = [0]*n
res = 0
sub = list()
final = list()
for i in range(0, n):
    a[i] = int(inp[i]);
a.sort();
for i in range(0, n):
    sub.append(a[i])
    for j in range(i+1, n):
        if a[j] - a[i] == 0 or a[j] - a[i] == 1:
            sub.append(a[j])
    count = len(sub)
    final.append(count)
res = final[0] - res
for i in range(0, len(final) - 1):
        if final[i+1] - final[i] > res:
            res = final[i+1] - final[i]
        else:
            continue
print(res)
