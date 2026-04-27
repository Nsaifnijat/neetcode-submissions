class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxf = 0
        count = {}
        longest = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(count[s[right]], maxf)


            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left +=1
            
            longest = max(longest, right - left + 1)
        return longest