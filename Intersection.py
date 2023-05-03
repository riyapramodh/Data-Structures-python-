#intersection of two sorted arrays:
#naive method
def naive(arr1,arr2):
    temp = []
    for i in arr1:
        for j in arr2:
            if i == j:
                if i not in temp:
                    temp.append(i)
    return temp

print(naive([3,5,10,10,10,15,15,20],[5,10,10,15,30]))



#efficient method
def efficient(arr1,arr2):
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if i>0 and arr1[i] == arr1[i-1]:
            i+=1
            continue

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print("[",arr1[i],"]")
            i += 1
            j += 1
            #we can use a temp array if we want to avoid the printing of None because this is not a void array thereby returning the temp array with the stored repeating elements


print(efficient([3,5,10,10,10,15,15,20],[5,10,10,15,30]))
