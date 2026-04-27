class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        prev = []

        for num in nums:
            if num in prev:
                return True
            prev.append(num)
        return False