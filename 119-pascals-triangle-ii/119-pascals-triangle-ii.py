from numpy.polynomial.polynomial import polypow
class Solution(object):
    def getRow(self, rowIndex):
        return [int(i) for i in polypow((1, 1), rowIndex)]