def bianrysort_naive(arr):
    n = len(arr)
    c = 0
    for i in range(0,n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

def binarysort_eff(arr):
    n = len(arr)
    swapped = False
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

print(bianrysort_naive([2,10,8,7]))
print(binarysort_eff([2,10,8,7]))
