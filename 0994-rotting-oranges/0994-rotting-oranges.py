class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m = rows, n = cols
        # 0 = empty cell, 1 = fresh orange, 2 = rotten orange
        #technique to be used Grid - BFS 
        # 4 dim = Top (-1,0), down (1,0), right (0,1), left (0,-1)
        # if all oranges cannot be rotten return -1

        #if the grid is empty or length is 0 return 0
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0

        #count the total number of fresh oranges
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j]==2):
                    q.append((i,j))
                elif (grid[i][j]==1):
                    fresh+=1 # count the total number of non empty cells
        
        if fresh==0:
            return 0
        
        #Directions in which it can turn fresh to rotten
        directions=([1,0],[-1,0],[0,1],[0,-1])
        minutes=0 #initialise the time 

        # Perform the BFS
        while q:
            size=len(q)
            for _ in range(size): 
                #ensure that takes (0,0) and then (0,3) in one iteration
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx, y+dy
                    if(
                        nx<0 or nx>=rows or
                        ny<0 or ny>=cols 
                    ):
                        continue
                    #Only fresh can become rotten
                    if (grid[nx][ny]!=1):
                        continue
                    #make it rotten
                    grid[nx][ny]=2
                    # one lesser fresh orange
                    fresh-=1
                    #append it to the queue
                    q.append((nx,ny))
            if q:
                minutes+=1
        return minutes if fresh==0 else -1