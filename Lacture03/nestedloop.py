#for hours in range(24):
#    for minutes in range(60):
#        for seconds in range(60):
#            print(hours, ':',minutes, ':', seconds)

columns = int(input('How many colume? '))

for h in range(101):
    for c in range(1, columns+1):
       print (h + c, end=' ')
    print()