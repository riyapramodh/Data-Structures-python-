#to see if the sum of any two elements in the array is equal to that of a given value
def naive(arr,s,n):
    for i in range(0,n-1):
        i = i+1
        for j in range(1,n-1):
            if arr[i] + arr[j] == s:
                return True
            else:
                j = j+1
    return False

def search(arr,s,n):
    i = 0
    j = n-1
    while i<=j:
        if arr[i]+arr[j]>s: #if the sum of the two numbers are greater than the given number we decrement the end pointer by one
            j = j - 1
        if arr[i]+arr[j]<s:#if the sum of the two numbers are lesser than the given number then we increment the head pointer by one
            i = i + 1
        if arr[i] + arr[j] == s:
            return True
    return False
print(naive([2,3,8,11],14,4))
print(search([2,3,8,11],14,4))
