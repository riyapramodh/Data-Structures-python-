class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        cols = collections.defaultdict(set) #cols is the key and set is the value in the  key - value pair
        rows = collections.defaultdict(set) 
        square = collections.defaultdict(set)
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or 
                    board[i][j] in square[i//3,j//3]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                square[i//3,j//3].add(board[i][j])
        return True
                    

                

                    
        
