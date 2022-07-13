class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return min(letters,key = lambda x: (ord(x) - 1) % ord(target))
        