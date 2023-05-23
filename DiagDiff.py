def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    suml = 0
    sumr = 0
    low = 0
    high = n-1
    for i in range(len(arr)):
        suml += arr[i][low]#when i = 0 and low = 0 it checks for 0th row 0th column when i = 1 and low+=1 becomes 1 it cheks for first row first column hence and son on...entire diagonal matrix is found
        sumr += arr[i][high]
        low+=1
        high-=1
        
    if sumr>suml:
        diff = sumr - suml
    else:
        diff = suml - sumr
        
    return diff
