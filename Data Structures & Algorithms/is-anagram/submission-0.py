class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        res = [0]*26

        for cs, ct in zip(s, t):
            res[ord(cs) - ord('a')] += 1
            res[ord(ct) - ord('a')] -= 1
        
        return all(c==0 for c in res)