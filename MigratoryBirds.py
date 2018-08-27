n = input()
arr = list(map(int, input().split(' ')))

ct1 = arr.count(1)
ct2 = arr.count(2)
ct3 = arr.count(3)
ct4 = arr.count(4)
ct5 = arr.count(5)

list = [ct1, ct2, ct3, ct4, ct5]
larger = list[0]
for i in range(0, len(list)-1):
    if list[i] > list[i+1] and list[i] > larger:
        larger = list[i]
        index = i
    elif list[i] == list[i+1] and list[i] > larger:
        larger = list[i]
        index = i
    elif list[i] < list[i+1] and list[i+1] > larger:
        larger = list[i+1]
        index = i+1
print(index+1)
