#method 1
class Solution(object):
    def generate_rows(self,row):
        arr = []
        ans = 1
        arr.append(ans)
        for col in range(0,row):
            ans = ans*(row-col)//(col+1)
            arr.append(ans)
        return arr
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(0,numRows):
            output.append(self.generate_rows(i))
        return output



#method 2

class Solution(object):
   if numRows == 0:
            return []
        tria = [[1]]
        for i in range(1,numRows):
            prev_row = tria[i-1]
            new_row = [1]
            for j in range(1,i):
                new_row.append(prev_row[j-1]+prev_row[j])
            new_row.append(1)
            tria.append(new_row)

        return tria
