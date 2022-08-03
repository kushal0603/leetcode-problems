class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
	
		# TC, SC = O(N); where N is the number of the elements in the matrix.
		
        # In this problem:
        # we are turning clockwise whenever we exceed a row or column
        # boundary or if we reach a already visited element
		
        if len(matrix) == 0:
            return matrix
			
        row,col = len(matrix),len(matrix[0])
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        # defining the possible positions of movement along x and y dir"
        x,y = 0,0
        di = 0
        # di represents the current dir" we are facing
        seen = [[0 for j in range(col)] for i in range(row)]
        # seen is used to keep track of elements that we have already seen
        ans = []
        for i in range(row*col):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dx[di]
            # next candidate position -> x + which dir" to head
            cc = y + dy[di]
            # similarly next candidate position for y 
            if cr >=0 and cr<row and cc >=0 and cc<col and not(seen[cr][cc]):
                x = cr
                y = cc
            else:
                di = (di+1)%4
                # %4 because after right->down->left->up
                # we repeat i.e. start back at right-> down....
                x += dx[di]
                y += dy[di]
        return ans