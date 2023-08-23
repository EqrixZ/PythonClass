def isValidIP(ip):
    string = ip.split(".")

    if len(string) == 4:
        print("True")
    else:
        print("False")

    return 

print(isValidIP("1.2.3.4"))
print(isValidIP("1.2.3"))
print(isValidIP("1.2.3.4.5"))
print(isValidIP("123.45.67.89"))
print(isValidIP("123.456.78.90"))
print(isValidIP("123.045.067.089"))