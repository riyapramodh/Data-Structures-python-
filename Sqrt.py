def sqrt(x):
    if x == 0 or x == 1:
        return x
    i = 1
    result = 1
    while result<=x:
        i+=1
        result = i*i
    return i -1

print(sqrt(9))
