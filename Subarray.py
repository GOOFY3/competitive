a = [1,-3,2,-5,7]
sublist = []
newsum = 0
sum = a[0]
for i in range(0, len(a)):
    for j in range(i+1, len(a)+1):
        sub = a[i:j]
        sublist.append(sub)
        print(sublist)

for i in range(0, len(sublist)):
    newsum = 0
    for j in range(0, len(sublist[i])):
        newsum = newsum + (sublist[i])[j];
    if newsum > sum:
        sum = newsum

print(sum)
