class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != ".":
                    if (c, i) in seen or (j, c) in seen or (i // 3, j // 3, c) in seen:
                        return False
                    seen.add((c, i))
                    seen.add((j, c))
                    seen.add((i // 3, j // 3, c))
        return True