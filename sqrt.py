#naive method
def sqrt(x):
    i = 0
    while (i*i) <= x:
        i = i+1
    return i+1
print(sqrt(9))

#binary search method
def sqrt(x):
    low = 1
    high = x
    ans = -1
    while low <= high:
        mid = (low+high)//2
        sqrt = mid*mid
        if sqrt == x:
            return mid
        elif sqrt < x:
            low = mid + 1
            ans = mid
            #this is the case when sqrt is lesser than or moreover equal to x
            #that sqrt value's mid we store as answer and the last value of ans saved from the last iteration is returned 
            #here for x is 10 , under sqrt the nearest sqrt is 9 of all so we take its mid, which is 3 store in ans and return it
        else:
            high = mid - 1
            # we only save the ans for the values of sqrt that are slightly lesser than or equal to the given x value
            #we then take the mid used for computing the sqrt and store it in the asnwer
    return ans

print(sqrt(10))


