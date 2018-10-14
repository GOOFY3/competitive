n1 = int(input())
arr1 = input().split(" ")
n2 = int(input())
arr2 = input().split(" ")

index = 0
res = set()

for i in range(0, n1):
    arr1[i] = int(arr1[i])
for i in range(0, n2):
    arr2[i] = int(arr2[i])

for i in range(0, n2):
    arr1.append(arr2[i])
    res = set(arr1)
    result = list(res)
    result.sort()
    for j in range(0, len(result)):
        # reverse result
        if(arr2[i] == result[j]):
            print(len(result) - j)
