class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        # BFS Logic
        # Queue to store nodes to visit next
        queue = [(entrance[0], entrance[1])]
        # To make sure we won't visit same cells again, we are setting visited cells to "+"
        maze[entrance[0]][entrance[1]] = "+"
        # Number of steps
        steps = 0
        # Current level size
        currentSize = 1
        # Next level size
        nextSize = 0

        while queue:
            # row, col to visit
            row, col = queue.pop(0)
            # We visited one cell of current level, so reducing currentSize by 1
            currentSize -= 1
            # If row, col cell is a border we reached the end of maze. So return steps
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1): return steps
            # Top, Bottom, Left, Right cell indices
            directions = {(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)}

            for direction in directions:
                # If cell is not out of maze and it doesn't have a wall, add it to queue and
                # increasing next level size by 1 and set it as visited by placing "+"
                if 0 <= direction[0] < len(maze) and 0 <= direction[1] < len(maze[0]) and maze[direction[0]][direction[1]] == ".":
                    maze[direction[0]][direction[1]] = "+"
                    queue.append(direction)
                    nextSize += 1
            # If we visited all nodes in current level
            if currentSize == 0:
                # We increase steps by 1
                steps += 1
                # nextSize becomes currentSize
                currentSize = nextSize
                # next size becomes 0
                nextSize = 0
        # We reach out of loop if we can't reach border cells. So return -1
        return -1