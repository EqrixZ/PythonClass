hour = int(input('What is your hours worked? '))
rate = float(input('What is your hourly pay rate? '))
if hour <= 40:
    print('Your gross pay is: $',format(hour*rate, '.2f'))
else:
    print('Your gross pay is: $',format(40*rate+(hour-40)*1.5*rate, '.2f'))
