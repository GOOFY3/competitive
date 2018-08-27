time = input()
newtime = list()
for i in range(2,8):
    newtime.append(time[i])

hours = int(time[0] + time[1])

if time[8] == 'P' and hours < 12:

    hours = str(hours + 12)
    add = list(hours)
    res = add + newtime
    for i in range(0, len(res)):
        print(res[i], end="")
else:
    hours = int(time[0] + time[1])
    if time[8] == 'A' and hours == 12:
        hours = str(hours - 12)
        add = list(hours)
        add = add + [0]
        res = add + newtime
        for i in range(0, len(res)):
            print(res[i], end="")
    else:
        for i in range(0,8):
            print(time[i], end="")
