rows = int(input('How many rows? '))
colums = int(input('How many columns? '))

for r in range(rows):
    for c in range(colums-1):
        print("*",end='')
    print("*")