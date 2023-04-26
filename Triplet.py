def naive(arr,s,n):
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == s:
                    return True
    return False

def search(arr,s,n):
    i = 0
    j = n-1
    while i <= j:
        k = arr[i]
        y = s - arr[i]
        if arr[i]+arr[j]>y:
            j = j - 1
        if arr[i]+arr[j]<y:
            i = i+1
        if arr[i]+arr[j] == y:
            print(arr[i]+arr[j]+k)
            return True

    return False

print(naive([2,3,5,6,15],20,5))
print(search([2,3,5,6,15],20,5))
