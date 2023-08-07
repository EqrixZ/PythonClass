enter = str(input('Enter a string: '))
print('This is what I found about that string:')
enter_string = enter.split()

if enter.isalnum():
    print("The string is alphanumeric.")
if enter.isalpha():
    print("The string contains only alphabetic characters.")
if enter.islower():
    print("The letters in the string are all lowercase.")
elif enter.isupper():
    print("The letters in the string are all uppercase.")  
if enter.isnumeric():
    print("The string contains only digits.")