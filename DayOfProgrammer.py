year = int(input())

leap = False
if year > 1918:
    if year%4==0 and year%100!=0 or year%400==0:
        leap = True
    else:
        leap = False
    if (leap):
        print("12.09." + str(year))
    else:
        print("13.09." + str(year))
if year < 1918:
    if year % 4 == 0:
        leap = True
    if (leap):
        print("12.09." + str(year))
    else:
        print("13.09." + str(year))

if year == 1918:
    print("26.09."+str(year))
