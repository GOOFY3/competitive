n1 = raw_input()
n2 = raw_input()
temp = 1

for i in range(1, int(n1)+1):
    if int(n1)%i == 0 and int(n2) % i == 0:
        if i > temp:
            temp = i
        else:
            continue

print(temp)
