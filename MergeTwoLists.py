x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
y = [1, 8, 9, 10, 15]

# for i in range(0, len(x)):
#     for j in range(i+1, len(x)):
#         if x[j] < x[i]:
#             temp = x[j]
#             x[j] = x[i]
#             x[i] = temp
#         else:
#             continue
# print(len(x))
ct = x.count(0)
for i in range(0, ct):
    x.remove(0)


for i in range(0, len(y)):
    for j in range(i+1, len(y)):
        if y[j] < y[i]:
            temp = y[j]
            y[j] = y[i]
            y[i] = temp
        else:
            continue
z = [0]*(len(x) + len(y) -1)
m = 0
n = 0
k = 0

while m <len(x) and n< len(y):
    if x[m] < y[n]:
        z[k] = x[m]
        m+=1
        n+=1
        k+=1
    elif x[m] > y[n]:
        z[k] = y[n]
        m+=1
        n+=1
        k+=1
    while(m < len(x)):
        z[k] = x[m]
        m += 1
        k += 1
    while(n < len(y)):
        z[k] = y[n]
        n += 1
        k += 1

print(z)
