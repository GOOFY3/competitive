inp = input().split(' ')
n = int(inp[0])
k = int(inp[1])

bill = input().split(' ')

for i in range(0, n):
    bill[i] = int(bill[i])

contribution = int(input())

sum = 0

for i in range(0, n):
    if i != k:
        sum = sum + bill[i]
split = sum/2

if contribution - split == 0:
    print("Bon Appetit")
else:    
    print(int(contribution - split))
