class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        num_dict = {}
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        
        
        for key,value in num_dict.items():
            buckets[value].append(key)
        
        
        res = []
        
        for i in range(len(buckets)-1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res