
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = s.lower()
        left = 0
        right = len(s)-1
        while left < right:
            while s[left].isalnum() != True and left < right:
                left +=1
            while s[right].isalnum() != True and left < right:
                right -= 1
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
            
        return True


                
