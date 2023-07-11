def quick(arr, low, high):
    i = low
    j = high
    pIndex = low
    while i < j:
        if arr[i] <= pIndex and i <= high - 1:
            i += 1
        if arr[j] > pIndex and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
    return j
