class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,ans = 0,0,0
        d = {}
        
        while j < len(s):
            if s[j] not in d or i > d[s[j]]:
                ans = max(ans, j-i+1)
                d[s[j]] = j
            else:
                i = d[s[j]] + 1
                ans = max(ans, j-i+1)
                j-=1
            j+=1
        return ans