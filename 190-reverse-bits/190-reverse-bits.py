class Solution:
    def reverseBits(self, n):
        return int("0b" + bin(n)[2:].rjust(32, "0")[::-1], 2)
