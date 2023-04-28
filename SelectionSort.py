def selectionsort(arr,n):
    for i in range(n-1):#changing range from n to n-1 is the optimisation here as the last element need not be sorted always

        minInd = i
        for j in range(i+1,n):
            if arr[j]<arr[minInd]:
                minInd = j
        arr[i],arr[minInd] = arr[minInd],arr[i]
    return arr

print(selectionsort([10,5,8,20,2,18],6))
