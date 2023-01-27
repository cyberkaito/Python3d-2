monthes = [31,28,31,30,31,30,31,31,30,31,30,31]

year = input("Enter year: ")
year = int(year)
if year % 4 == 0:
    print("Year is leap")
    monthes[1] = 29
if year % 4 != 0:
    print("Year isn't leap")
    monthes[1] = 28
i = 0
summa = 0
while i < len(monthes):
    g = 1
    while g <= monthes[i]:
        if len(str(g)) == 1:
            summa += g
        elif len(str(g)) == 2:
            summa += int(g / 10)
            summa += g % 10   
        g += 1
    i += 1
print(summa)

