def sqrt(x):
    if x == 0 or x == 1:
        return x
    i = 1
    result = 1
    while result<=x: #result is the array that stores the value an di is the pointer so as long as the result is lee or equal to the number(say 1.5*1.5 = 3 if equal to x <= 4, as long as it is small we increment i vale so as to reach the maximum possible value sof product of i(i*i = result)which is smaller than x)

        i+=1
        result = i*i
    return i -1 #suppose the current value of the result is smaller than x and we hence continue inside the loop but then after loop execution the value got incremented; then we break out of the loop and return i-1; the nearest value of i for which it was closest tox being same or less than x


print(sqrt(9))
