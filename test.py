x = str(input())


b = [0]*len(x)

def subsetinOnes(n):
        b.append(n)

def subsetinTwos(n):
        b.append(n)

for i in range(0, n):
    for j in range(i, i+2):
        two = int(a[i] + a[j])
        one = int(a[i])
        if temp < 27:
            subsetinTwos(two)
        else:
            subsetInOnes(one)
