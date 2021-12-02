# Hash map based
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i,j in enumerate(nums):
            x = target - j
            if x in d:
                return([d[x], i])
            d[j] = i