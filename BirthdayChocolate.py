num = input()
arr = input().split(' ')
d, m = input().split(' ')

sum = 0
count = 0

for i in range(0, int(num)-int(m)+1):
    for j in range(0, int(m)):
        sum = sum + int(arr[i+j])
    if sum == int(d):
        count = count + 1
    sum = 0

print(count)
