class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        g = sorted(nums.copy())
        if len(nums) == 2:
            return [0,1]
        a = 0 
        b = len(nums)-1
        
        while a != b:
            if g[a] + g[b] == target:
                if nums.index(g[a]) == nums.index(g[b]):
                    res = [x for x in range(len(nums)) if nums[x] == g[b]]
                    return [res[0], res[1]]
                return [nums.index(g[a]),nums.index(g[b])]
            elif g[a] + g[b] > target:
                b -= 1
            else:
                a +=1