class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        prev = {}
        left = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in prev:
                left = max(prev[s[r]] + 1, left)
            
            prev[s[r]] = r
            longest = max(longest, r - left +1)
        return longest
            