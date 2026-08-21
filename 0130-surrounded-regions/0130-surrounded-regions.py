class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if set of X connected to O's in boundaries then cannot convert to X

        #check condition 
        if not board or not board[0]:
            return 0
        rows = len(board)
        cols = len(board[0])
        directions = ([1,0],[-1,0],[0,1],[0,-1])
        def dfs(r,c):
            # Check Boundaries
            if (
                r<0 or r>=rows or
                c<0 or c>=cols or
                board[r][c]!="O"
            ):
               return
            # Mark boundary connected O's as safe
            board[r][c]="S"
            #visit all 4 directions
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                dfs(nr,nc)
        
        #Find all 0's connected to boundaries
        #1. First and Last Row
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        #2. First and Last Coloumn
        for r in range(rows):
            #first col
            if board[r][0]=="O":
                dfs(r,0)
            #last col
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
        
        #Convert Surrouneded O to X, Safe O to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="S":
                    board[r][c]="O"    