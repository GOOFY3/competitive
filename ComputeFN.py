n = raw_input()
arr = [0]*int(n)

for i in range(0,int(n)):
    arr[i] = raw_input()

for i in range(0,int(n)):
    arr[i] = int(arr[i])

def calc(num):
    if num % 2 == 0:
        print(num/2)
    else:
        print(-num/2)
        
for n in arr:
    calc(n)
