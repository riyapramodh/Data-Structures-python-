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


"""
the loop runs from the first element to the last element
explanation:first we assign the first element as the key and store the previous element in a variable j
the while loop is executed under the condition that it runs as long as the jth element is greater than 0 and the prev element to the key is greater than key and if it satisfies the condition it enters into the loop else it goes to the part where the key is getting overwritten by its own self 
if the condition in the while loop would have been satisfied then the key element value gets overwritten by the value of the previous element j and the index of j will go one unit backwards and then when it tries to execute the loop of while again :if j  = 0 it will beocome j = j-1 = -1 and wont satisfy the first cndition or else in some other case it mit not satisfy the second condition and comes out of the loop and the next element becomes the key 
