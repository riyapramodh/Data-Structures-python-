def naive(arr,n):  #O(n**2)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]

def naive2(arr,n):#O(nlogn)    #not recomended as it is changing the original array
    arr.sort()
    for i in range(0, n-1):
        if arr[i] == arr[i+1]:
            return arr[i]
def naive3(arr,n): #O(n)
    visited = []
    for i in range(0,n-1):
        visited.append(False)

    for j in range(0,n):
        if visited[arr[j]]:
            return arr[j]
        visited[arr[j]] = True





print(naive([0,2,1,3,2,2],6))
print(naive2([0,2,1,3,2,2],6))
print(naive3([0,2,1,3,2,2],6))



#EFFICIENT METHOD

def efficient(arr):
    slow = arr[0]
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    return arr[slow]

def efficient2(arr,n):
    slow = arr[0]
    fast = arr[n-1]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
        return slow

print(efficient([1,3,2,4,6,5,7,3]))
print(efficient2([1,3,2,4,6,5,7,3],8))
