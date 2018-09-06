n = int(input())
inp = [0]*n
for i in range(0, n):
    inp[i] = str(input())
q = int(input())
queries = [0]*q
for i in range(0, q):
    queries[i] = str(input())

for i in range(0, q):
    temp = queries[i]
    count = 0
    for j in range(0,n):
        if inp[j] == temp:
            count = count + 1
    print(count)
