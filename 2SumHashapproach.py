#hash table method to see if the sum of two num in an array is eq to target:
def check(arr,target):
    hash = {}
    for i,num in enumerate(arr): #i is the index and num is the ele at that index --> in this  manner we will apend it into the hash table
        x = target - num
        if x in hash:
            return [hash[num],i]
        hash[num] = i
    return []
