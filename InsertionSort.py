def insertionsort(arr,n):
    for i in range(1,n):
        key = arr[i]#the first value in index 1 is stored in a paointer key
        j = i -1 #the value j will store the index of the previous value to that of the arr[i]
        while j >= 0 and arr[j]>key: #as long as the value of j is not ;ess than 0 and as long as the jth element is greater than key (key stores the smaller values)
          #here we dont use >= and just use > because it reduces unstability condition
            arr[j+1] = arr[j] #as the element gets inserted in between of the sorted part of the array, it expands and there will be a shift in the index position of the nearby elements by a unit of 1
            j = j-1
        arr[j+1] = key #initially key is the first index but after completioin of first sort then the index position gets incremented by 1
    return arr
print(insertionsort([20,5,40,60,10,30],6))
