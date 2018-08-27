n, k = input().split(' ')
arr = input().split(' ')

count = 0
sum = 0

for i in range(0, int(n)):
    for j in range(i+1, int(n)):
        sum = int(arr[i]) + int(arr[j])
        if sum % int(k) == 0:
            count = count + 1

print(count)
