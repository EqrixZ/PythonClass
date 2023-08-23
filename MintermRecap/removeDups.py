def removeDups(num):
    if not num:
        return []

    array = str(num[0])
    for s in num[:1]:
        i = 0
        while array[i] == s[i]:
            array = array[:i]
        
    return array

print(removeDups([1, 0, 1, 0]))
print(removeDups(["The", "big", "cat"]))
print(removeDups(["John", "Taylor", "John"]))