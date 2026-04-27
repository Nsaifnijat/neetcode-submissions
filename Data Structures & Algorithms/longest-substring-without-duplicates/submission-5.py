class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = {}
        left = 0
        longest = 0
        for right in range(len((s))):
            if s[right] in prev:
                left = max(prev[s[right]] + 1, left)
            prev[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest