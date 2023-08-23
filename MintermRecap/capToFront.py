def capToFront(word):
    word = str(word)
    upletter = ""
    lwletter = ""

    for i in word:
        if i.upper():
            i = upletter
        if i.lower():
            i = lwletter
    result = upletter 
        
        

print(capToFront("hApPy"))
print(capToFront("moveMENT"))
print(capToFront("shOrtCAKE"))