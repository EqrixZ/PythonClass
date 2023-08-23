def numSplit(num):
    return [num//2, num//2 + num%2]

print(numSplit(4))
print(numSplit(10))
print(numSplit(11))
print(numSplit(-9))