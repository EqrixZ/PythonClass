#for hours in range(24):
#    for minutes in range(60):
#        for seconds in range(60):
#            print(hours, ':',minutes, ':', seconds)

columns = int(input('How many columns? '))

for h in range(1, 101, columns):
    for c in range(columns):
        num = h + c
        if num <= 100:
            print(num, end=' ')
    print()