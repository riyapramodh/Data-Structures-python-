#to find the median after adding two dorted arrays
# def search(arr1,arr2,n,m):
#     low1 = 0
#     high1 = n - 1
#     while low1<=high1:
#         mid1 = (low1+high1)//2
#         # leftpart = arr1[0:mid1]
#
#         mid2 = (m/2)-mid1-2
#         # leftpart2 = arr2[0:mid2]
#         if arr2[mid2]<arr1[mid1+1]:
#             low1 = mid1+1
#         else:
#             mid2 = mid2 - mid1
#         if arr1[mid1+1]<arr2[mid2+1] and arr2[mid2+1]<arr1[mid1+1]:
#             median = (max(arr1[mid1],arr2[mid2]) + max(arr1[mid1],arr2[mid2]))//2
#             return median
#     return False
# print(search([1,2,3,4,5],[1,2,3,4,5,6,7,8],5,8))
#
#
def func(arr1,arr2):
    A, B = arr1, arr2
    total = len(A)+len(B)
    half = total//2

    if len(A)>len(B):
        A,B = B,A
    l,r = 0,len(A)-1
    while True:
        i = (l+r)//2
        j = half - i -2
        Aleft = A[i] if i>=0 else float("-infinity")
        Aright = A[i+1] if i+1 <len(A) else float("infinity")
        Bleft = B[j] if j>=0 else float("-infinity")
        Bright = B[j+1] if j+1 < len(B) else float("infinity")


        if Aleft <= Bright and Bleft <= Aright:
            if total %2:
                return min(Aright, Bright)
            return (max(Aleft,Bleft) + min(Aright, Bright)) // 2
        elif Aleft> Bright:
            r = i - 1
        else:
            l = i + 1

print(func([],[1,2,3,4,5,6,7,8]))
