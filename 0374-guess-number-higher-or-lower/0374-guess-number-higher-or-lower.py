class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            guess_res = guess(mid)
            if guess_res == 0:
                return mid
            elif guess_res == 1:
                left = mid + 1
            else:
                right = mid - 1