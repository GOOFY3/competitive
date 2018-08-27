a = [0,0,1,0,1,0,0]
sublist = []
newsum = 0
sum = a[0]
count = 0
for i in range(0, len(a)):
    for j in range(i+1, len(a)+1):
        sub = a[i:j]
        sublist.append(sub)

for i in range(0, len(sublist)):
    newsum = 0
    for j in range(0, len(sublist[i])):
        newsum = newsum + (sublist[i])[j];
    zero = sublist[i].count(0)
    one = sublist[i].count(1)
    if zero == one:
        print(sublist[i])
