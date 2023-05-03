#union of two sorted arrays
def naive(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    arr3 = []
    for i in range(0,n):
        arr3.append(arr1[i])
    for j in range(0,m):
        arr3.append(arr2[j])
    arr3.sort()
    for k in range(0,len(arr3)):
        if k==0 or arr3[k] != arr3[k-1]:
            print(arr3[k])
#print(naive([10,20,20],[5,20,40,40]))

def efficient(arr1,arr2):
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    while i<n and j<m:
        if i>0 and arr1[i] == arr1[i-1]:#if i is greater than 0 and ith element is equal to prev element we dont go to the main loop but we just incremenet the i value and continue
            i+=1
            continue
        if j>0 and arr2[j]==arr2[j-1]:
            j+=1
            continue
        if arr1[i]<arr2[j]:
            print(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            print(arr2[j])
            j+=1
        else:
            print(arr1[i])
            i+=1
            j+=1

    #there mit still be elements remaining in any of the array so we need to complete the printing of them hence:
    while i<n:
        if i>0 and arr1[i]!=arr1[i-1]:#if i is greater than 0 and ith element is not same as previous element print
            print(arr1[i])
        i+=1
    while j<m:
        if j>0 and arr2[j]!=arr2[j-1]:
            print(arr2[j])
        j+=1


print(efficient([10,20,20],[5,20,40,40]))
