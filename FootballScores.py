#given the scores of two teams teamA and teamB we need to find for each element on teamB how many elements are ther ein teamA smaller than the teamB's particular element

def search(teama,teamb):
    n = len(teama)
    arr = []
    teama.sort()
    for i in teamb:
        low = 0
        high = len(teama) - 1
        while low<=high:

            mid = (low+high)//2
            if i < teama[mid]:
                high = mid-1
            else:
                low = mid+1
        arr.append(low)
    return arr



print(search([1,2,3],[2,4]))

