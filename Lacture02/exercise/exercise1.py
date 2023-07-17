#Get the user test score
first = int(input('Enter your first test score: '))
second = int(input('Enter your second test score: '))
third = int(input('Enter your third test score: '))
#Calculate the average
average = (first+second+third)/3
#Display the average
print("this is your average score: ",format(average, '.2f'))
if average > 95 :
    print("Congratulate!")
    print("That is a great average!")