#insert in a maxheap
def insert(arr,x,n):

    arr[n+1] = x
    i = n
    while i>1:
        parent = i/2
        if arr[parent]<arr[i]:
            arr[parent],arr[i] = arr[i],arr[parent]
            i = parent#now we start from the i's parent value as the new i value and calculate its parent value and so on...
        else:
            continue
    return arr

print(insert([50,40,45,30,20,35,10],60,7))
