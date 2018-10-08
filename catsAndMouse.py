n = int(input())
arr = list()
l = list()
for i in range(0, int(n)):
  x = input().split(" ")
  arr.append(x)

for i in range(0, n):
    for j in range(0, 3):
        arr[i][j] = int(arr[i][j]);

for i in range(0 , n):
    cata = arr[i][0];
    catb = arr[i][1];
    mouse = arr[i][2];
    dis1 = mouse - cata;
    dis2 = catb - mouse;
    if dis1 < 0:
        dis1 = -1 * dis1
    if dis2 < 0:
        dis2 = -1 * dis2
    if dis1 < dis2:
        print("Cat A")
    elif dis2 < dis1:
        print("Cat B")
    else:
        print("Mouse C")
