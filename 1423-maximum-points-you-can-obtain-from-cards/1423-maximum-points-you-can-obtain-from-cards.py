class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #def maxScore(self, cardPoints: List[int], k: int) -> int:
	    cur_sum = max_sum = sum(islice(cardPoints, k))
	    left_ind = k
	    for i in cardPoints[ :len(cardPoints) - 1 - k: -1]:
		    cur_sum += i
		    k -= 1
		    cur_sum -= cardPoints[k]
		    max_sum = max(max_sum, cur_sum)
	    return max_sum