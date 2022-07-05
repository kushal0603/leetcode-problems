class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            pivot = left + (right - left)//2
            if guess(pivot) == 0:
                return pivot
            if guess(pivot) == 1:
                left = pivot + 1
            elif guess(pivot) == -1:
                right = pivot - 1
        return left