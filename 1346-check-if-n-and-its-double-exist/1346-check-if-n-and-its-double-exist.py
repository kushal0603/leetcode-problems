class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return arr.count(0) > 1 or len(set(x*2 for x in arr if x != 0).intersection(set(arr))) > 0 