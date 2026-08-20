class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m=rows and n=cols
        # map meaning => 1=land, 0=water
        #Island is surrounded by water 
        # continuous land patches = 1 island
        if not grid or not grid[0]:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        directions=([1,0],[-1,0],[0,1],[0,-1])
        for i in range(rows):
            for j in range(cols):
                # if we find land we found new island - to find the starting node
                if grid[i][j]=="1":
                    islands+=1
                    q=deque()
                    q.append((i,j))
                    grid[i][j]="0" #marked as visited
                    # performing BFS once the starting nodes are determined
                    while q:
                        x,y=q.popleft()
                        for dx,dy in directions:
                            nx=x+dx
                            ny=y+dy
                            #Check Boundaries
                            if(
                                nx<0 or nx>=rows or
                                ny<0 or ny>=cols
                                ):
                                   continue
                            #if not land continue or VISIT ONLY LAND
                            if(grid[nx][ny]!="1"):
                                continue
                            grid[nx][ny]="0" #mark as visted
                            q.append((nx,ny))
        return islands