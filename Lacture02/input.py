# Get the user's first name.
#first_name = input('Enter your first name: ')

#Get the user's last name.
#last_name = input('Enter your last name: ')

#print a greeting to the user.
#print('Hello',first_name , last_name)

# Get the user's name, age, and income.
#name = input('What is your name? ')
#age = int(input('What is your age? '))
#income = float(input('What is your income? '))

# Display the data.
#print('Here is the data your enterend:')
#print('Name:',name)
#print('Age:',age)
#print('Income: ', format(income, '12,.2f'))

# Get the user's hour,rate
hour = int(input('What is your hours worked? '))
rate = float(input('What is your hourly pay rate? '))
cal = hour*rate

# Display
print('Your gross pay is:',format(cal, '.2f'))