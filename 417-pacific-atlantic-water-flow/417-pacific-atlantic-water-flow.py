class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row = len(heights)
        num_col = len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(row, col, sea, height):
            """DFS traversal to mark which "land" is efficient for the water to flow from the sea into the land (increasing land's values)
            @Param:
            - row: row index
            - col: col index
            - sea: pacific or atlantic sea, used to mark if the land is eligible for water to flow
            - height: height of the current land
            """
            queue = collections.deque()
            sea.add((row, col))
            
            # we will keep track of the current land position and its height to check for condition below
            queue.append((row, col, height))
            
            # 4 directions - NEWS
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
			# while there are still lands to be visited
            while queue:
                # get the row, col and height of the current (main) land
                curr_row, curr_col, curr_height = queue.pop() # <<<<< if you want BFS, change this to queue.popleft()
                
                # visit all 4 NEWS directions
                for dr, dc in directions:
                    # update position
                    row = curr_row + dr
                    col = curr_col + dc
                    
                    # check if the new land's position is in the bound and whether we have not visited it
                    if (row in range(num_row)) and (col in range(num_col)) and ((row, col) not in sea):
                        
                        # here, it is en eligible land, calculate its height
                        height = heights[row][col]
                        
                        # the new land (neighbor)'s height must be large than the previous (main) land's height
                        if height >= curr_height:
                            
                            # marked we already visited it and put into the queue
                            sea.add((row, col))
                            queue.append((row, col, height))
        
        # DFS from top and bottom row and mark which land able to have water flow to pacific or atlantic accordingly
        for col in range(num_col):
            dfs(0, col, pac, heights[0][col])
            dfs(num_row - 1, col, atl, heights[num_row - 1][col])
            
        # DFS from left and right row and mark which land able to have water flow to pacific or atlantic accordingly
        for row in range(num_row):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, num_col - 1, atl, heights[row][num_col - 1])
        
        res = []
        
        # visit each node and mark which land are able to water flow to pacific AND atlantic
        for row in range(num_row):
            for col in range(num_col):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])
                    
        return res
    
