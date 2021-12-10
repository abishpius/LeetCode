class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = nums1 + nums2
        comb.sort()
        if len(comb)%2 == 1:
            return comb[len(comb)//2]
        else:
            return((comb[len(comb)//2] + comb[len(comb)//2 - 1])/2)