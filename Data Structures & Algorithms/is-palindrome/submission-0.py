class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        while left < right:
            # 1) Move left pointer forward past non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # 2) Move right pointer backward past non-alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # 3) Compare the characters (in lowercase)
            if s[left].lower() != s[right].lower():
                return False

            # 4) Advance both pointers toward the middle
            left += 1
            right -= 1

        # If we never found a mismatch, it's a palindrome
        return True